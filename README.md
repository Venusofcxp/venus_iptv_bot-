# 📺 VENUS IPTV BOT - Script Automatizado com Firebase, Telegram e FCM

Este projeto busca automaticamente **filmes, séries, temporadas e episódios** de uma API IPTV e os envia para o Firebase. Ele também notifica via **FCM (Firebase Cloud Messaging)** sempre que um novo conteúdo for detectado, e possui um **bot no Telegram** com comandos úteis.

---

## ⚙️ Funcionalidades

✅ Busca **automática de filmes e séries** via API IPTV  
✅ Consulta **detalhes de cada série** (temporadas e episódios)  
✅ Envia tudo para o **Firebase Realtime Database**  
✅ Notifica novos lançamentos via **FCM Push Notification**  
✅ Bot do Telegram com botões:
- 🔍 Buscar
- 🆕 Mostrar recentes
- 🎬 Ver quantidade

---

## 🛠️ Requisitos

- Python 3.8+
- VPS ou computador Linux/Windows
- Conta no Firebase com projeto Realtime Database
- Token do seu bot do Telegram
- Chave FCM para notificações

---

## 📁 Estrutura do projeto

```
venus_iptv_bot/
├── .env                      # Variáveis de ambiente (tokens, URLs)
├── main.py                   # Script principal (executa bot + verificação por hora)
├── iptv_fetcher.py           # Busca IPTV e episódios
├── firebase_service.py       # Integração com Firebase
├── notifier.py               # Envia notificações FCM
├── telegram_bot.py           # Bot Telegram com comandos
├── history.json              # Controle de IDs já adicionados
├── requirements.txt          # Dependências do projeto
├── credencial-firebase.json  # Suas credenciais do Firebase
```

---

## 📦 Instalação

```bash
# 1. Clone o projeto
git clone https://github.com/SEU_USUARIO/venus_iptv_bot.git
cd venus_iptv_bot

# 2. Crie ambiente virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Adicione seu arquivo credencial-firebase.json

# 5. Configure o .env com:
# - Token do Bot Telegram
# - URL do Firebase
# - Chave FCM

# 6. Execute
python main.py
```

---

## 🕒 Execução automática

O script já é configurado para rodar automaticamente a cada 1 hora (via `time.sleep(3600)` dentro de uma thread).

Se quiser rodar via cron, edite o agendamento com:

```bash
crontab -e

# Exemplo para rodar a cada hora:
0 * * * * cd /caminho/do/projeto && /caminho/do/python3 main.py
```

---

## 🧠 Sobre a API IPTV usada

- Busca de filmes: `action=get_vod_streams`
- Busca de séries: `action=get_series`
- Detalhes: `action=get_series_info&series_id=...`

---

## 📲 Exemplo de notificação

```
Título: The Flash - Temporada 9
Sinopse: Barry volta no tempo para impedir uma catástrofe.
Imagem: exibida como banner (via FCM)
```

---

## 🧑‍💻 Autor

Criado por: **FLASH TÚNEL / VenusPlay**

Se curtiu, ⭐ o projeto no GitHub!
