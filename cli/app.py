import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write, read
import tempfile
from text2speech import text2speech
from speech2text import speech2text
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from groq_service import execute

def record_audio(duration=9, fs=44100):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    print("Recording finished")

    # Save the recording to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".wav")
    write(temp_file.name, fs, recording)

    return temp_file.name

def play_audio(audio_file_path):
    fs, data = read(audio_file_path)
    sd.play(data, fs)
    sd.wait()

def main():
    while True:
        audio_file_path = record_audio()

        text = speech2text(audio_file_path)
        generated_answer = execute(f"Please answer to the question: {text}")
        generated_speech = text2speech(generated_answer)

        play_audio(generated_speech)

        # Ask the user if they want to continue
        user_input = input("Press 'q' to quit or any other key to continue: ")
        if user_input.lower() == 'q':
            break

if __name__ == '__main__':
    main()