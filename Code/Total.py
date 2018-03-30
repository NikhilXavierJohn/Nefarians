from pytube import YouTube
import os
from pydub import AudioSegment
from moviepy.editor import *
import speech_recognition as sr
from tqdm import tqdm
from shutil import copyfile
import time
from pydub.silence import detect_nonsilent




def download(ytb):
    yt = YouTube(str(ytb))
    dest = os.path.dirname('C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/InputFile/')
    opt=input("Would you like to rename the file (Y/N)")
    if(opt=='Y'):
        filename=input("Enter a filename :")
        yt.streams.filter(subtype='mp4').first().download(dest,filename=filename)
        
    else:
        yt.streams.filter(subtype='mp4').first().download(dest)
        
    print("file has been successfully downloaded")
    converter('C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/InputFile/'+str(filename),filename)


def converter(video,filename):
    clip = VideoFileClip(str(video))
    print("Video Length :"+str(clip.duration))
    clip = VideoFileClip(str(video)).subclip(0,clip.duration)
    filename=str(filename)+".wav"
    clip.audio.write_audiofile(filename,progress_bar=True)
    copyfile(filename, "C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/audio/"+filename)
    copyfile(filename, "C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/InputFile/"+filename)
    os.rename("C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/audio/"+filename,"C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/split/file1.wav")
    copyfile("C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/InputFile/"+filename, "C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/audio/"+filename)
    os.remove(filename)
    findSound(filename)

def findSound(filename):
    sound = AudioSegment.from_wav(filename)
    val=sound.dBFS
    k=val-20
    print(val)
    print(len(sound))
    a=(detect_nonsilent(sound,min_silence_len=3400, silence_thresh=k,seek_step=1))
    size=len(a)
    for i in range(size):
        t1=a[i][0]
        t2=a[i][1]
        silenceSplitter(filename,t1,t2,(i+1))
    filename=filename
    splitter(filename)

def silenceSplitter(filename,t1,t2,i):
    clip = AudioSegment.from_wav(filename)
    newAudio = clip[t1:t2]
    newAudio.export("file1_"+str(i)+'.wav', format="wav")
    

def splitter(filename):   
    t1=0
    t2=30000
    i=0
    os.chdir("C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/split/")
    clip = AudioSegment.from_wav('file1.wav')
    while(float((t2/1000)<=float(clip.duration_seconds))):
            clip = AudioSegment.from_wav('file1.wav')
            newAudio = clip[t1:t2]
            t1 = t1 + 30000 
            t2 = t1 + 30000
            newAudio.export("file1_"+str(i)+'.wav', format="wav")
            i+=1
            if(i==7):
                i=0
                os.remove("file1.wav")
                transcribe()
                removefiles()
                os.rename("C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/audio/"+filename,"C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/split/file1.wav")
                copyfile("C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/InputFile/"+filename, "C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/audio/"+filename)
                os.chdir("C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/split/")

    leftover=(float(clip.duration_seconds)*1000) -t2+30000
    print("Remaining clip :"+str(leftover))
    os.remove("file1.wav")
    if(leftover>0):
        t1=t2-30000
        t2=t1+(leftover)
        newAudio = clip[t1:t2]
        newAudio.export("file1_"+str(i)+'.wav', format="wav")
        time.sleep(2)
        transcribe()



def silenceSplitter(t1,t2,i):
    clip = AudioSegment.from_wav('file1.wav')
    newAudio = clip[t1:t2]
    newAudio.export("file1_"+str(i)+'.wav', format="wav")
    

def removefiles():
    folder = 'C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/split'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
    
def transcribe():
    r = sr.Recognizer()
    files = os.listdir('C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/split')
    
    all_text = []
    
    for f in tqdm(files):
        name = "C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/split/" + f
        with sr.AudioFile(name) as source:
            audio = r.record(source)
        text = r.recognize_bing(audio, " 109f5d904f2c40c7b6c31beb3b5a09c4")
        all_text.append(text)
    
    transcript = ""
    for i, t in enumerate(all_text):
        total_seconds = i * 30
        m, s = divmod(total_seconds, 60)
        h, m = divmod(m, 60)
        transcript = transcript + "{:0>2d}:{:0>2d}:{:0>2d} {}\n".format(h, m, s, t)
    
    print(transcript)
    
    with open("C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/transcription.txt", "a") as f:
        f.write(transcript)

findSound("C:/Users/nikhi/OneDrive/Documents/GitHub/Nefarians/Code/01_Course_Introduction_14-11.wav")