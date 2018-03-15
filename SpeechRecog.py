import speech_recognition as sr
r = sr.Recognizer()
with sr.WavFile("converted.wav") as source:              # use "test.wav" as the audio source
    audio = r.record(source)                        # extract audio data from the file

try:
    print("Transcription: " + r.recognize_bing(audio," fabd259c7b944600b89f7515edd6d9ea"))   # recognize speech using Google Speech Recognition
except LookupError:                                 # speech is unintelligible
    print("Could not understand audio")