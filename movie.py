import os
from moviepy.editor import *
clip = VideoFileClip("01_Course_Introduction_14-11.mp4")
print(clip.duration)
clip = VideoFileClip("01_Course_Introduction_14-11.mp4").subclip(0,clip.duration)
filename="01_Course_Introduction_14-11.wav"
clip.audio.write_audiofile(filename,progress_bar=True)
os.rename("01_Course_Introduction_14-11.wav","./spilt/01_Course_.wav")


