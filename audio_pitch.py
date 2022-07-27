import os
from tkinter import *
from tkinter import messagebox, filedialog

import audio_functions
from utils import mp3TypeValid, wavTypeValid


def main(root):
    global editor
    editor = Toplevel(root)
    editor.geometry("400x200")
    editor.title("Audi Pitching")
    editor.config(bg='#535356')
    global addFile;
    addFile=Button(editor, text="Choose a file", command=lambda window=editor:openFile(window,1))
    addFile.grid(row=0,column=0,padx=2,pady=1)

def createLayout(editor,name):
    global container
    container=Frame(editor)
    container.grid(row=0,column=0,columnspan=2)
    Label1=Label(container,text="File opened:",fg="black",font= ('Arial'))
    Label1.grid(row=0,column=0,padx=5,pady=8,sticky="n",)
    fileName_Label=Label(container,text=name,fg="black",bd=2,font= ('Helvetica 15 underline'))
    fileName_Label.grid(row=0,column=1,padx=1,pady=8,sticky="n",)
    fileName_Label.config(text = name)
    button=Button(container,text="Choose another file", command=lambda window=editor:openFile(window,2))
    button.grid(row=0,column=2,padx=5)
    frame = Frame(container, bd=2, relief="raised", width=350,height=20)
    frame.grid(column=0, row=1, columnspan=4,ipadx=5,ipady=2, padx=5,pady=5,sticky=(N, S, E, W))


    speed_lbl=Label(frame,text="Shift by ",fg="Red", font=("Helvetica", 10)).grid(row=2,column=0)
    # Create Dropdown menu
    options = [
        "-5",
        "-4",
        "-3",
        "-2",
        "-1",
        "1",
        "2",
        "3",
        "4",
        "5"
    ]
    # datatype of menu text
    clicked = StringVar()
    # initial menu text
    clicked.set("Choose steps")

    def onChange(*args):
        global steps
        steps= clicked.get()
        show_buttons(steps)
    clicked.trace('w', onChange)

    drop = OptionMenu(frame, clicked, *options).grid(row=2,column=1)
    def show_buttons(steps):
        numofsteps = steps[-1:]
        numofsteps = int(numofsteps)
        sign=steps[0]
        if sign=="-":
            print("iam here")
            numofsteps=(numofsteps)*-1
        print(numofsteps)
        play_btn = Button(frame, text="Play", width=9, command=lambda x=1,fileName=name,speed=numofsteps: audio_functions.audioProcsess_func(x, fileName, speed,2))
        play_btn.grid(row=3, column=1, padx=1)
        plot_btn = Button(frame,text="Plot",width=9,command=lambda x=2,fileName=name,speed=numofsteps: audio_functions.audioProcsess_func(x,fileName,speed,2))
        plot_btn.grid(row=3, column=2, padx=1)
        save_btn = Button(frame,text="Save",width=9,command=lambda x=3,fileName=name,speed=numofsteps: audio_functions.audioProcsess_func(x,fileName,speed,2))
        save_btn.grid(row=3, column=3, padx=1)

def openFile(window,x):
        openedFilePath = filedialog.askopenfilename()
        openedFileName = os.path.basename(openedFilePath)
        if x==2:
            container.destroy()
        if wavTypeValid(openedFileName):
            createLayout(window,openedFileName)
        else:
            print("Unsupported format")
            # editor.destroy()


