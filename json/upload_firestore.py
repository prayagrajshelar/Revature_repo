import json
import os
from google.cloud import firestore

# Set Google Credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "firestore_key.json"

# Initialize Firestore client
db = firestore.Client()

# Open the newline-delimited JSON file
with open("comments_nd.json", "r") as f:
    for line in f:
        if line.strip():  # skip empty lines
            item = json.loads(line)
            doc_id = str(item["id"])  # Use "id" as Firestore document ID
            db.collection("comments").document(doc_id).set(item)

print("✅ All comments uploaded to Firestore.")
