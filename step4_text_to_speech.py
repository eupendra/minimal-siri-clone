import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

headers = {"Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"}

def text_to_speech(input_text):
    data = {
        "model": "tts-1",
        "input": input_text,
        "voice": "nova",
    }

    response = requests.post(
        "https://api.openai.com/v1/audio/speech", headers=headers, json=data
    )

    filename = "output.mp3"
    # Save to file
    with open(filename, "wb") as f:
        f.write(response.content)

    print(f"Saved {filename}")
    return filename


if __name__ == "__main__":
    text_to_speech("Hi! This is Siri.")