from vosk import (Model, KaldiRecognizer)
import pyaudio

# video tutorial => https://youtu.be/3Mga7_8bYpw?si=a04fIprhErF_qZm4

# Thoughts => Vosk is good but kind of slow out the box
# will experiment with DeepSpeech, AprilASR, etc

# change file path to your computer
small_model = (r"F:\steph\Documents\Github\Speech-To-Text-Converter\40MB-Vosk-English-Model\vosk-model-small-en"
                r"-us-0.15")
mac_small_model = (r"/Users/stepheno/Documents/GitHub/Speech-To-Text-Converter/40MB-Vosk-English-Model/vosk-model-small-en-us-0.15")

mac_med_model = (r"/Users/stepheno/Documents/GitHub/Speech-To-Text-Converter/128MB-Vosk-English-Model")

model = Model(mac_small_model)
recognizer = KaldiRecognizer(model, 16000)  # frequency

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    # if len(data) ==0:
    #     break
    if recognizer.AcceptWaveform(data):  # if model recognizes speech
        speech = recognizer.Result()
        text = speech[14:-3]  # get text from JSON output

        if text == "stop":
            exit(1)
        else:
            print(text)
