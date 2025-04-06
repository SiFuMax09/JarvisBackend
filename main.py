from fastapi import FastAPI, File, UploadFile, Form
import whisper

app = FastAPI()

# Preload the Whisper models globally
models = {
   # "tiny": whisper.load_model("tiny"),
   # "base": whisper.load_model("base"),
   # "small": whisper.load_model("small"),
   # "medium": whisper.load_model("medium"),
   # "large": whisper.load_model("large"),
    "turbo": whisper.load_model("turbo"),
}

print("Loaded models: " + ", ".join(models.keys()))

@app.post("/transcribe")
async def transcribe_audio(
        file: UploadFile = File(...),
        language: str = Form(None),
        model: str = Form("base")
):
    # Validate the model input
    if model not in models:
        return {"error": f"Invalid model '{model}'. Available models: {list(models.keys())}"}

    # Read the uploaded file and save it temporarily
    audio_data = await file.read()

    # Write the file to a local temporary audio file
    temp_audio_path = f"{file.filename}"
    with open(temp_audio_path, "wb") as f:
        f.write(audio_data)

    # Transcribe the audio using the selected model and optional language parameter
    selected_model = models[model]
    if language:
        result = selected_model.transcribe(temp_audio_path, language=language)
    else:
        result = selected_model.transcribe(temp_audio_path)

    # Return transcript
    return {"transcript": result["text"]}
