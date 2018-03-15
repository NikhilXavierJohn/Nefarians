from pydub import AudioSegment
from moviepy.editor import *
import os
t1=0
t2=30000
i=0
os.chdir("./spilt/")

clip = AudioSegment.from_wav('01_Course_.wav')
while(float((t2/1000)<=float(clip.duration_seconds))):
    clip = AudioSegment.from_wav('01_Course_.wav')
    newAudio = clip[t1:t2]
    t1 = t1 + 30000 #Works in milliseconds
    t2 = t1+30000
    newAudio.export("01_Course_"+str(i)+'.wav', format="wav")
    i+=1
leftover=(float(clip.duration_seconds)*1000) -t2+30000
#print(leftover)
if(leftover>0):
    t1=t2-30000
    t2=t1+(leftover)
    newAudio = clip[t1:t2]
    newAudio.export("01_Course_"+str(i)+'.wav', format="wav")
    