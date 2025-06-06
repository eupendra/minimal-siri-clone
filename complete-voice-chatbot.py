# import sounddevice as sd
# import soundfile as sf

# import requests
# import os
# from dotenv import load_dotenv
# load_dotenv()
# API_KEY = os.getenv("OPENAI_API_KEY")

# def record(duration=5, fs=44100):
#     print("Speak now...")
#     audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
#     sd.wait()
#     filename = "temp_audio.wav"
#     sf.write(filename, audio, fs)
#     return filename

# def audio_to_text(file_path):
#     with open(file_path, "rb") as f:
#         response = requests.post(
#             "https://api.openai.com/v1/audio/transcriptions",
#             headers={"Authorization": f"Bearer {API_KEY}"},
#             files={"file": f},
#             data={"model": "whisper-1"}
#         )
#     return response.json()["text"]

# def get_response(text, previous_response_id=None):
#     payload = {
#         "model": "gpt-4o",
#         "input": text,
#         "instructions": "You are siri. You understnad indian english accent and replies with minimal words. All the input is strictly in english."
#     }
    
#     if previous_response_id:
#         payload["previous_response_id"] = previous_response_id
    
#     response = requests.post(
#         "https://api.openai.com/v1/responses",
#         headers={
#             "Authorization": f"Bearer {API_KEY}",
#             "Content-Type": "application/json"
#         },
#         json=payload
#     )
    
#     result = response.json()
#     response_text = result.get("output_text", result["output"][0]["content"][0]["text"])
#     return response_text, result["id"]

# def tts(text, output_path="response.mp3"):
#     response = requests.post(
#         "https://api.openai.com/v1/audio/speech",
#         headers={
#             "Authorization": f"Bearer {API_KEY}",
#             "Content-Type": "application/json"
#         },
#         json={
#             "model": "tts-1",
#             "input": text,
#             "voice": "nova"
#         }
#     )
#     with open(output_path, "wb") as f:
#         f.write(response.content)
#     os.system(f"afplay {output_path}")

# def main():
#     print("Say 'bye' to exit chat.")
#     last_response_id = None

#     while True:
#         audio_path = record(duration=6)
#         try:
#             user_input = audio_to_text(audio_path)
#             print("You:", user_input)

#             if "bye" in user_input.lower():
#                 print("\n\nYou said bye. Exiting...")
#                 break

#             reply, last_response_id = get_response(user_input, last_response_id)
            
#             print("Bot:", reply)
#             print("Generating audio...")
#             tts(reply)
#             print(f"\n\nConversation ID: {last_response_id}")
#             print("Ready for next question.")

#         except Exception as e:
#             print(f"Error: {e}")
#             last_response_id = None

# if __name__ == "__main__":
#     main()
