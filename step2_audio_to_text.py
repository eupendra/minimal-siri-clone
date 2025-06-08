import whisper
import os

# Load a lightweight Whisper model for faster transcription
model = whisper.load_model("tiny")

def audio_to_text(file_path):
    # Use local whisper model instead of API call
    result = model.transcribe(file_path)
    print(result["text"])
    return result["text"]

def audio_to_text_api(file_path):
    """Legacy function for OpenAI API - keeping for reference"""
    import requests
    from dotenv import load_dotenv
    
    load_dotenv()
    api_key = os.getenv("OPENAI_API_KEY")
    
    with open(file_path, "rb") as f:
        response = requests.post(
            "https://api.openai.com/v1/audio/transcriptions",
            headers={"Authorization": f"Bearer {api_key}"},
            files={"file": f},
            data={"model": "whisper-1"},
        )
    print(response.json()["text"])
    return response.json()["text"]

if __name__ == "__main__":
    audio_to_text("temp_audio.wav")
