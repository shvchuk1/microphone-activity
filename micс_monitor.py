import sounddevice as sd
import numpy as np

THRESHOLD = 0.4  # sensitivity (0–1)

def audio_callback(indata, frames, time, status):
    volume = np.linalg.norm(indata) * 10
    volume = round(float(volume), 2)

    if volume > THRESHOLD:
        print(f"⚠️ Sound detected! ({volume})")
    else:
        print(f"Volume: {volume}")

def main():
    print("🎤 Microphone monitor started (CTRL + C to stop)")
    with sd.InputStream(callback=audio_callback):
        while True:
            sd.sleep(100)

if __name__ == "__main__":
    main()
