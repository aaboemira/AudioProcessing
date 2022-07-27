import os

import audio_pitch
import audio_timeScale
import speech_to_text
import utils
from audio_functions import plot_func, mp3_converter
import sounddevice as sd
from tkinter import *
import queue
import soundfile as sf
import threading
import wave
import matplotlib.pyplot as plt

from tkinter import messagebox, filedialog

from pydub import AudioSegment
from pyrubberband import pyrb



def voice_record():
    voice_rec = Toplevel(root)
    voice_rec.geometry("360x200")
    voice_rec.title("Voice Recorder")
    voice_rec.config(bg="#107dc2")
    # Label to display app title
    title_lbl = Label(voice_rec, text="Voice Recorder", bg="#107dc2").grid(row=0, column=0,columnspan=3)

    # Create a queue to contain the audio data
    q = queue.Queue()
    # Declare variables and initialise them
    recording = False
    file_exists = False

    # Fit data into queue
    def callback(indata, frames, time, status):
        q.put(indata.copy())

    # Functions to play, stop and record audio
    entry = Entry(voice_rec, width=20)
    entry.focus_set()
    # The recording is done as a thread to prevent it being the main process
    def threading_rec(x):
        name = entry.get()
        if name:
            if x == 1:
                # If recording is selected, then the thread is activated
                t1 = threading.Thread(target=record_audio,args=(name,))
                t1.start()
                print(threading.active_count())
            elif x == 2:
                # To stop, set the flag to false
                global recording
                recording = False
                messagebox.showinfo(message="Recording finished")
            elif x == 3:
                # To play a recording, it must exist.
                try:
                    data, fs = sf.read(name, dtype='float32')
                    sd.play(data, fs)
                    sd.wait()
                except:
                    messagebox.showinfo(message="Please record a file")
        else:
            messagebox.showinfo(message="Please enter a file name")

    # Recording function
    def record_audio(fileName):
        # Declare global variables
        global recording
        # Set to True to record
        recording = True
        global file_exists
        # Create a file to save the audio
        messagebox.showinfo(message="Recording Audio. Speak into the mic")
        with sf.SoundFile(fileName, mode='w', samplerate=44100,
                          channels=2,format="wav") as file:
            # Create an input stream to record audio without a preset time
            with sd.InputStream(samplerate=44100, channels=2, callback=callback):
                while recording == True:
                    # Set the variable to True to allow playing the audio later
                    file_exists = True
                    # write into file
                    file.write(q.get())


    # Button to record audio
    record_btn = Button(voice_rec, text="Record Audio", command=lambda m=1: threading_rec(m))
    # Stop button
    stop_btn = Button(voice_rec, text="Stop Recording", command=lambda m=2: threading_rec(m))
    # Play button
    play_btn = Button(voice_rec, text="Play Recording", command=lambda m=3: threading_rec(m))

    # Position buttons
    record_btn.grid(row=2, column=0)
    stop_btn.grid(row=2, column=1)
    play_btn.grid(row=2, column=2)
    entry.grid(row=1,column=1,pady = 2)


def timeScale():
    audio_timeScale.main(root)

def audioPitch():
    audio_pitch.main(root)
def voice_text():
    filename = filedialog.askopenfilename()
    name = os.path.basename(filename)
    if (utils.wavTypeValid(name)):
        t2 = threading.Thread(target=speech_to_text.audio_to_text, args=(name,root))
        t2.start()

def plot():
    filename = filedialog.askopenfilename()
    name= os.path.basename(filename)
    if(utils.wavTypeValid(name)):
        plot_func(name)

def convertListenr():
    filename = filedialog.askopenfilename()
    name = os.path.basename(filename)
    if(utils.mp3TypeValid(name)):
        mp3_converter(name)


root = Tk()
root.geometry('200x300')

btn = Button(root, text="Record an audio", command = voice_record)
btn2 = Button(root, text="Plot a wave", command = plot)
btn3 = Button(root, text="Audio speed ",command=timeScale)
btn4 = Button(root,text="Audio pitch",command=audioPitch)
btn5 = Button(root, text="Voice to text", command = voice_text)
btn6 = Button(root,text="Convert to wav",command=convertListenr)

btn.pack(pady = 10)
btn2.pack(pady = 10)
btn3.pack(pady = 10)
btn4.pack(pady = 10)
btn5.pack(pady=10)
btn6.pack(pady=10)


root.mainloop()
