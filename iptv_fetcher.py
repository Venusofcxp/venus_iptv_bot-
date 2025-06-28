import requests, json, os
from firebase_service import enviar_firebase
from notifier import notificar_fcm

FILMES_URL = "https://prime.cnfl.xyz/player_api.php?username=VenusPlay&password=67964995&action=get_vod_streams"
SERIES_URL = "https://prime.cnfl.xyz/player_api.php?username=VenusPlay&password=67964995&action=get_series"
SERIES_INFO_URL = "https://prime.cnfl.xyz/player_api.php?username=VenusPlay&password=67964995&action=get_series_info&series_id="
HISTORY_FILE = "history.json"

def carregar_historico():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, 'r') as f:
            return json.load(f)
    return {"filmes": [], "series": [], "episodios": []}

def salvar_historico(data):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(data, f)

def verificar_novos_conteudos():
    hist = carregar_historico()
    
    # FILMES
    r = requests.get(FILMES_URL).json()
    for item in r:
        if str(item["stream_id"]) not in hist["filmes"]:
            filme = {
                "Título": item.get("name", ""),
                "Capa": item.get("stream_icon", ""),
                "Score": item.get("rating", ""),
                "Ano": item.get("year", ""),
                "Tipo": "Filme",
                "ID": item.get("stream_id"),
                "Gênero": item.get("category_name", ""),
                "Sinopse": item.get("plot", ""),
                "Banner": item.get("backdrop_path", "")
            }
            enviar_firebase("filmes", filme)
            notificar_fcm(filme["Título"], filme["Sinopse"], filme["Capa"])
            hist["filmes"].append(str(item["stream_id"]))

    # SÉRIES + TEMPORADAS + EPISÓDIOS
    r = requests.get(SERIES_URL).json()
    for item in r:
        series_id = str(item["series_id"])
        if series_id not in hist["series"]:
            serie = {
                "Título": item.get("name", ""),
                "Capa": item.get("cover", ""),
                "Score": item.get("rating", ""),
                "Ano": item.get("releaseDate", ""),
                "Tipo": "Série",
                "ID": series_id,
                "Gênero": item.get("category_name", ""),
                "Sinopse": item.get("plot", ""),
                "Banner": item.get("backdrop_path", "")
            }
            enviar_firebase("series", serie)
            notificar_fcm(serie["Título"], serie["Sinopse"], serie["Capa"])
            hist["series"].append(series_id)

        # TEMPORADAS + EPISÓDIOS
        r_info = requests.get(SERIES_INFO_URL + series_id).json()
        if "seasons" in r_info:
            for temporada in r_info["seasons"]:
                temp_num = str(temporada["season_num"])
                for ep in temporada.get("episodes", []):
                    ep_id = str(ep["id"])
                    if ep_id not in hist["episodios"]:
                        episodio = {
                            "ID": series_id,
                            "Temporada": temp_num,
                            "Episodio": str(ep.get("episode_num")),
                            "Titulo_EP": ep.get("title", ""),
                            "Capa_EP": ep.get("info", {}).get("movie_image", ""),
                            "Play": ep.get("url", ""),
                            "Sinopse_EP": ep.get("info", {}).get("plot", "")
                        }
                        enviar_firebase("episodios", episodio)
                        notificar_fcm(f"Novo EP: {episodio['Titulo_EP']}", episodio["Sinopse_EP"], episodio["Capa_EP"])
                        hist["episodios"].append(ep_id)

    salvar_historico(hist)
