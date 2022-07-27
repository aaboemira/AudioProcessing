import os

import audio_pitch
import audio_record
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


def main():
    global root
    root = Tk()
    root.geometry('200x300')

    btn = Button(root, text="Record an audio", command=recordAudio)
    btn2 = Button(root, text="Plot a wave", command=plot)
    btn3 = Button(root, text="Audio speed ", command=timeScale)
    btn4 = Button(root, text="Audio pitch", command=audioPitch)
    btn5 = Button(root, text="Voice to text", command=voice_text)
    btn6 = Button(root, text="Convert to wav", command=convertListenr)

    btn.pack(pady=10)
    btn2.pack(pady=10)
    btn3.pack(pady=10)
    btn4.pack(pady=10)
    btn5.pack(pady=10)
    btn6.pack(pady=10)

    root.mainloop()


def recordAudio():
    audio_record.main(root)
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

main()