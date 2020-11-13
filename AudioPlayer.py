from tkinter import*
from tkmacosx import Button
import sounddevice as sd
from scipy.io.wavfile import write
import pyaudio
import wave
root=Tk()

##def sound():
##    fs=44100
##    seconds=3
##
##    myrecording=sd.rec(int(seconds*fs), samplerate=fs, channels=2)
##    sd.wait()
##    write('output.wav', fs, myrecording)
##    
##play=Button(root, command=sound)
##
##play.pack()

chunk=1024
sample_format=pyaudio.paInt16
channels=1
fs=44100
seconds=3
filename='output.wav'

p=pyaudio.PyAudio()

print('Recording')

stream=p.open(format=sample_format,
              channels=channels,
              rate=fs,
              frames_per_buffer=chunk,
              input=True)

frames=[]

for i in range (0,int(fs/chunk*seconds)):
    data=stream.read(chunk)
    frames.append(data)

stream.stop_stream()
stream.close()
p.terminate()

print('Finished recording')

wf=wave.open(filename,'wb')
wf.setnchannels(channels)
wf.setsampwidth(p.get_sample_size(sample_format))
wf.setframerate(fs)
wf.writeframes(b''.join(frames))
wf.close()

root.mainloop()
