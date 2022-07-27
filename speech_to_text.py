from speech_recognition import Microphone, Recognizer, UnknownValueError, AudioFile
from time import sleep
from tkinter import *


def callback(recognizer, source):
    try:
        recognized = recognizer.recognize_google(source)
        print(f"[+] You said\n{recognized}")
    except UnknownValueError:
        print("[-] Unable to recognize what you said")


def voice_to_text(duration):
    recog = Recognizer()
    mic = Microphone()
    with mic:
        recog.adjust_for_ambient_noise(mic, duration=1)

    print("[+] Talk...")
    stop_listenning = recog.listen_in_background(mic, callback)
    sleep(duration)
    stop_listenning()


def audio_to_text(filename,root):
    recog = Recognizer()
    with AudioFile(filename) as file:
        audio = recog.record(file)
    textWindow(root,recog.recognize_google(audio))

def textWindow(root,text):
    editor = Toplevel(root)
    editor.geometry("200x150")
    editor.title("Lyrics")
    label1=Label(editor,fg="Black",text="You said!",font="Arial 16")
    label2=Label(editor,fg="Black",text=text,wraplength=120)
    label1.pack()
    label2.pack()