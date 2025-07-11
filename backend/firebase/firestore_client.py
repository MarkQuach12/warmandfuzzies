import os
from google.cloud import firestore

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "firebase/firebase-key.json"

db = firestore.Client()