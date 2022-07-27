from tkinter import messagebox

import soundfile as sf
import sounddevice as sd
from matplotlib import pyplot as plt
from pydub import AudioSegment
from pyrubberband import pyrb


def audioProcsess_func(x,fileName,speed,type):
    s, rate = sf.read(fileName)
    # sd.play(s, rate)
    # sd.wait()
    if type==1:
        edited_Audio = pyrb.time_stretch(s, rate, speed)
    elif type==2:
        edited_Audio = pyrb.pitch_shift(s, rate, speed)
    if x == 1:
        sd.play(edited_Audio)
    elif x == 2:
        print("iam here")
        fig, axs = plt.subplots(2)
        fig.suptitle('Time scaling of wave')
        axs[0].plot(s,color="blue")
        axs[1].plot(edited_Audio,color="blue")

        plt.ylabel("Amplitude")
        plt.show()
    elif x==3:
        sf.write("output.wav",edited_Audio,rate,format='wav')
        messagebox.showinfo(title="File saved", message="file saved as output.wav")
def plot_func(fileName):
    # Label to display app title
        s, rate = sf.read(fileName)
        plt.title("waveform of wave")
        plt.plot(s, color="blue")
        plt.ylabel("Amplitude")
        plt.show()

def mp3_converter(input_file):
    output_file = input_file[:-4]
    try:
        sound = AudioSegment.from_mp3(input_file)
        sound.export(output_file, format="wav")
        messagebox.showinfo(title="File converted succefully",message="File has been converted successfully")
    except:
        messagebox.showinfo(title="Problem with file",message="File didn't convert ")