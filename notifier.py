import requests
import os
from dotenv import load_dotenv
load_dotenv()

def notificar_fcm(titulo, mensagem, imagem):
    url = "https://fcm.googleapis.com/fcm/send"
    headers = {
        "Authorization": f"key={os.getenv('FCM_SERVER_KEY')}",
        "Content-Type": "application/json"
    }
    payload = {
        "to": "/topics/all",
        "notification": {
            "title": titulo,
            "body": mensagem,
            "image": imagem
        },
        "priority": "high"
    }
    requests.post(url, headers=headers, json=payload)
