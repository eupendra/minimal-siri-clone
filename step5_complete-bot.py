from step1_record_audio import record
from step2_audio_to_text import audio_to_text
from step3_get_response import get_response
from step4_text_to_speech import text_to_speech
import os

def main():
    print("Say 'bye' to exit chat.")

    while True:
        audio_path = record(duration=6)
        try:
            user_input = audio_to_text(audio_path)
            # print("You:", user_input)

            if "bye" in user_input.lower():
                print("\n\nYou said bye. Exiting...")
                break

            reply = get_response(user_input)
            print("Generating audio...")
            fname = text_to_speech(reply)
            os.system(f"afplay {fname}")
            print("Ready for next question.")

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
