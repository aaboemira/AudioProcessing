import queue
import threading
import soundfile as sf
import sounddevice as sd
from tkinter import *
from tkinter import messagebox


def main(root):
    voice_rec = Toplevel(root)
    voice_rec.geometry("360x200")
    voice_rec.title("Voice Recorder")
    voice_rec.config(bg="#107dc2")
    # Label to display app title

    title_lbl = Label(voice_rec, text="Voice Recorder", bg="#107dc2").grid(row=0, column=0,columnspan=3)
    # Create a queue to contain the audio data
    global q
    q = queue.Queue()
    # Declare variables and initialise them
    recording = False
    file_exists = False
    global entry
    entry = Entry(voice_rec, width=20)
    entry.focus_set()
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
def callback(indata, frames, time, status):
    q.put(indata.copy())


