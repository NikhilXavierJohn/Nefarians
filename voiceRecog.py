import speech_recognition as s
a=s.Recognizer()

#file="Converted.wav"

with s.Microphone() as source:
    print("Say Something")
    listener=a.listen(source)
    print("processing")

try:
    text=a.recognize_google(listener)
    print(text)
except Exception as e:
    print(e)