from pytube import YouTube
import os
from pydub import AudioSegment
from moviepy.editor import *
import speech_recognition as sr
from tqdm import tqdm
from shutil import copyfile


def download():
    yt = YouTube(str(input("Enter the video link: ")))
    dest = os.path.dirname('D:\\')
    opt=input("Would you like to rename the file (Y/N)")
    if(opt=='Y'):
        filename=input("Enter a filename :")
        yt.streams.filter(subtype='mp4').first().download(dest,filename=filename)
    else:
        yt.streams.filter(subtype='mp4').first().download(dest)
    print("file has been successfully downloaded")


def converter():
    clip = VideoFileClip("01_Course_Introduction_14-11.mp4")
    print("Video Length :"+str(clip.duration))
    clip = VideoFileClip("01_Course_Introduction_14-11.mp4").subclip(0,clip.duration)
    filename="01_Course_Introduction_14-11.wav"
    clip.audio.write_audiofile(filename,progress_bar=True)
    copyfile("01_Course_Introduction_14-11.wav", "D:/nlp/01_Week_1_-_Course_Introduction/audio/01_Course_Introduction_14-11.wav")
    os.rename("D:/nlp/01_Week_1_-_Course_Introduction/audio/01_Course_Introduction_14-11.wav","./spilt/01_Course_.wav")
    copyfile("D:/nlp/01_Week_1_-_Course_Introduction/01_Course_Introduction_14-11.wav", "D:/nlp/01_Week_1_-_Course_Introduction/audio/01_Course_Introduction_14-11.wav")
    splitter()
    




def splitter():   
    t1=0
    t2=30000
    i=0
    path=os.getcwd()
    os.chdir("./spilt/")
    clip = AudioSegment.from_wav('01_Course_.wav')
    while(float((t2/1000)<=float(clip.duration_seconds))):
            clip = AudioSegment.from_wav('01_Course_.wav')
            newAudio = clip[t1:t2]
            t1 = t1 + 30000 
            t2 = t1+30000
            newAudio.export("01_Course_"+str(i)+'.wav', format="wav")
            i+=1
            if(i==7):
                i=0
                os.remove("01_Course_.wav")
                transcribe()
                removefiles()
                os.rename("D:/nlp/01_Week_1_-_Course_Introduction/audio/01_Course_Introduction_14-11.wav","D:/nlp/01_Week_1_-_Course_Introduction/spilt/01_Course_.wav")
                copyfile("D:/nlp/01_Week_1_-_Course_Introduction/01_Course_Introduction_14-11.wav", "D:/nlp/01_Week_1_-_Course_Introduction/audio/01_Course_Introduction_14-11.wav")
                os.chdir("D:/nlp/01_Week_1_-_Course_Introduction/spilt/")

    leftover=(float(clip.duration_seconds)*1000) -t2+30000
    #print(leftover)
    if(leftover>0):
        t1=t2-30000
        t2=t1+(leftover)
        newAudio = clip[t1:t2]
        newAudio.export("01_Course_"+str(i)+'.wav', format="wav")
        transcribe()

def removefiles():
    folder = 'D:/nlp/01_Week_1_-_Course_Introduction/spilt/'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
            #elif os.path.isdir(file_path): shutil.rmtree(file_path)
        except Exception as e:
            print(e)
    
def transcribe():
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
    
    with open("D:/nlp/01_Week_1_-_Course_Introduction/01_Week_1_-_Course_.txt", "a") as f:
        f.write(transcript)

download()