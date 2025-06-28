import firebase_admin
from firebase_admin import credentials, db
import os
from dotenv import load_dotenv

load_dotenv()

cred = credentials.Certificate(os.getenv("FIREBASE_CREDENTIALS"))
firebase_admin.initialize_app(cred, {
    'databaseURL': os.getenv("FIREBASE_DB")
})

def enviar_firebase(categoria, data):
    ref = db.reference(f"/Venus/{categoria}")
    ref.push().set(data)
