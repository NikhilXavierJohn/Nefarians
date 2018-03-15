from pytube import YouTube
import os
yt = YouTube(str(input("Enter the video link: ")))
dest = os.path.dirname('D:\\')
opt=input("Would you like to rename the file (Y/N)")
if(opt=='Y'):
    filename=input("Enter a filename :")
    yt.streams.filter(subtype='mp4').first().download(dest,filename=filename)
else:
    yt.streams.filter(subtype='mp4').first().download(dest)
print("file has been successfully downloaded")