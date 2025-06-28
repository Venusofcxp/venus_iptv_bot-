import time
import threading
from iptv_fetcher import verificar_novos_conteudos
from telegram_bot import iniciar_bot

def loop_busca():
    while True:
        verificar_novos_conteudos()
        time.sleep(3600)  # Executa de hora em hora

if __name__ == "__main__":
    threading.Thread(target=loop_busca).start()
    iniciar_bot()
