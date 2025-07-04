import sounddevice as sd
import soundfile as sf


def record(duration=3, sample_rate=44100):
    """Record a short audio clip from the microphone."""
    print("Speak now...")
    audio = sd.rec(int(duration * sample_rate), channels=1, samplerate=sample_rate)
    sd.wait()
    filename = "temp_audio.wav"
    sf.write(filename, audio, sample_rate)
    print(f"Saved {filename}")
    return filename


if __name__ == "__main__":
    record()
