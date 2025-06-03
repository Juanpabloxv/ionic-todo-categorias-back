import firebase_admin
from firebase_admin import credentials
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CREDENTIALS_PATH = os.path.join(BASE_DIR, 'firebase_credentials', 'tu_archivo_de_servicio.json')

try:
    cred = credentials.Certificate(CREDENTIALS_PATH)
    firebase_app = firebase_admin.initialize_app(cred)
    print("Firebase app initialized successfully!")
except Exception as e:
    print(f"Error initializing Firebase app: {e}")
    firebase_app = None

def get_firestore_db():
    if firebase_app:
        from firebase_admin import firestore
        return firestore.client()
    return None

db = get_firestore_db()