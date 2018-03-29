import os
import speech_recognition as sr
from tqdm import tqdm
 

 
r = sr.Recognizer()
files = os.listdir('D:/nlp/01_Week_1_-_Course_Introduction/spilt/')
 
all_text = []
 
for f in tqdm(files):
    name = "D:/nlp/01_Week_1_-_Course_Introduction/spilt/" + f
    # Load audio file
    with sr.AudioFile(name) as source:
        audio = r.record(source)
    # Transcribe audio file
    text = r.recognize_bing(audio, " 109f5d904f2c40c7b6c31beb3b5a09c4")
    all_text.append(text)
 
transcript = ""
for i, t in enumerate(all_text):
    total_seconds = i * 30
    m, s = divmod(total_seconds, 60)
    h, m = divmod(m, 60)
 
    # Format time as h:m:s - 30 seconds of text
    transcript = transcript + "{:0>2d}:{:0>2d}:{:0>2d} {}\n".format(h, m, s, t)
 
print(transcript)
 
with open("01_Week_1_-_Course_.txt", "w") as f:
    f.write(transcript)
