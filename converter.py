from vosk import Model, KaldiRecognizer
import pyaudio

# video tutorial => https://youtu.be/3Mga7_8bYpw?si=a04fIprhErF_qZm4

# change file path to your computer
voskFilePath = (r"F:\steph\Documents\Github\Speech-To-Text-Converter\vosk-model-small-en-us-0.15\vosk-model-small-en"
                r"-us-0.15")

model = Model(voskFilePath)
recognizer = KaldiRecognizer(model, 16000)  # frequency

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
stream.start_stream()

while True:
    data = stream.read(4096)
    # if len(data) ==0:
    #     break
    if recognizer.AcceptWaveform(data):  # if model recognizes speech
        text = recognizer.Result()
        print(text[14:-3])
