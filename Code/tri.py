<<<<<<< HEAD
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
def findSound():
    sound = AudioSegment.from_wav("01_Course_Introduction_14-11.wav")
    val=sound.dBFS
    k=val-20
    print(val)
    print(len(sound))
    a=(detect_nonsilent(sound,min_silence_len=3400, silence_thresh=k,seek_step=1))
    size=len(a)
    for i in range(size):
        t1=a[i][0]
        t2=a[i][1]
=======
from pydub import AudioSegment
from pydub.silence import detect_nonsilent
def findSound():
    sound = AudioSegment.from_wav("01_Course_Introduction_14-11.wav")
    val=sound.dBFS
    k=val-20
    print(val)
    print(len(sound))
    a=(detect_nonsilent(sound,min_silence_len=3400, silence_thresh=k,seek_step=1))
    size=len(a)
    for i in range(size):
        t1=a[i][0]
        t2=a[i][1]
>>>>>>> 1dcb99b2c04475e04f8ef00d33975d2e16a57f2d
        silencesplitter(t1,t2,i+1)