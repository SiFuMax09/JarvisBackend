import requests

# Server-URL basierend auf Ihrem laufenden uvicorn-Server
url = "http://127.0.0.1:8000/transcribe"

# Pfad zur Audiodatei
audio_file_path = "./audio.mp3"

# Dateien und Parameter für die Anfrage
files = {
    'file': ('audio.mp3', open(audio_file_path, 'rb'), 'audio/mpeg')
}

# Formular-Parameter
data = {
    'model': 'tiny',
    # 'language': 'de'  # Optional, auskommentiert
}

# Anfrage senden
response = requests.post(url, files=files, data=data)

# Ergebnis ausgeben
if response.status_code == 200:
    result = response.json()
    print("Transkription erfolgreich:")
    print(result["transcript"])
else:
    print(f"Fehler bei der Transkription. Status-Code: {response.status_code}")
    print(response.text)