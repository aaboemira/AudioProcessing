import os
from tkinter import *
from tkinter import messagebox, filedialog

import audio_functions
from utils import  wavTypeValid


def main(root):
    editor = Toplevel(root)
    editor.geometry("360x300")
    editor.title("Time scale")
    editor.config(bg='#BF7C41')
    addFile=Button(editor, text="Choose a file", command=lambda window=editor:openFile(window))
    print("Iam here")
    addFile.grid(row=0,column=0,padx=2,pady=1)



def createLayout(editor,name):
    fileName_Label=Label(editor,text=name,fg="white",bg="black")
    fileName_Label.grid(row=0,column=1,padx=1,sticky="n")
    frame = Frame(editor, bd=2, relief="flat", width=350,height=20)
    frame.grid(column=0, row=1, columnspan=4,ipadx=5,ipady=2,sticky=(N, S, E, W))

    speed_lbl=Label(frame,text="Choose speed rate",fg="Red", font=("Helvetica", 10)).grid(row=2,column=0)
    # Create Dropdown menu
    options = [
        "0.25X",
        "0.5X",
        "0.75x",
        "1x",
        "1.5x",
        "2x",
        "3x",
    ]
    # datatype of menu text
    clicked = StringVar()
    # initial menu text
    clicked.set("Choose Speed")

    def onChange(*args):
        global speed
        speed= clicked.get()
        show_buttons(speed)
    clicked.trace('w', onChange)

    drop = OptionMenu(frame, clicked, *options).grid(row=2,column=1)
    def show_buttons(speed):
        speed = speed[:-1]
        speed=float(speed)
        play_btn = Button(frame, text="Play", width=9, command=lambda x=1,fileName=name,speed=speed: audio_functions.audioProcsess_func(x, fileName, speed,1))
        play_btn.grid(row=3, column=1, padx=1)
        plot_btn = Button(frame,text="Plot",width=9,command=lambda x=2,fileName=name,speed=speed: audio_functions.audioProcsess_func(x,fileName,speed,1))
        plot_btn.grid(row=3, column=2, padx=1)
        save_btn = Button(frame,text="Save",width=9,command=lambda x=3,fileName=name,speed=speed: audio_functions.audioProcsess_func(x,fileName,speed,1))
        save_btn.grid(row=3, column=3, padx=1)




def openFile(window):
    openedFilePath = filedialog.askopenfilename()
    openedFileName = os.path.basename(openedFilePath)

    if wavTypeValid(openedFileName):
        createLayout(window,openedFileName)
    else:
        print("Choose Another file")



