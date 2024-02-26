import hashlib
import json
from fastapi import FastAPI, UploadFile, File, Form

app = FastAPI()

def hash_variable_content(data):

    if isinstance(data, dict):
        hashed_data = {}
        for key, value in data.items():
            if isinstance(value, dict) or isinstance(value, list):
                hashed_data[key] = hash_variable_content(value)
            else:
                hashed_data[key] = hashlib.sha256(str(value).encode('utf-8')).hexdigest()
                if value is None:
                    hashed_data[key] = "0"  # Remplacer le hachage par "0" si la valeur est None
        return hashed_data
    elif isinstance(data, list):
        hashed_data = []
        for item in data:
            if isinstance(item, dict) or isinstance(item, list):
                hashed_data.append(hash_variable_content(item))
            else:
                hashed_item = hashlib.sha256(str(item).encode('utf-8')).hexdigest()
                if item is None:
                    hashed_item = "0"  # Remplacer le hachage par "0" si la valeur est None
                hashed_data.append(hashed_item)
        return hashed_data
    else:
        return data

# Déclarer les variables globales
json_contents = None
hashed_contents = None

@app.post("/upload/")
async def upload_json_file(file: UploadFile = File(...)):
    global json_contents, hashed_contents

    if file.content_type != "application/json":
        return {"error": "Le fichier doit être de type JSON"}

    contents = await file.read()
    json_contents = json.loads(contents)
    hashed_contents = hash_variable_content(json_contents)

    return {"message": "Fichier JSON téléchargé avec succès (haché)", "hashed_contents": hashed_contents}
