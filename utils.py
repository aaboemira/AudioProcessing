from tkinter import messagebox



def wavTypeValid(name):
    extenstion=name[-3:]
    if extenstion!="wav":
        messagebox.showerror(title="Unsupported Format",message="Please choose a wav file")
        print("Unsupported format")
        return False
    else:return True

def mp3TypeValid(name):
    extenstion=name[-3:]
    if extenstion!="mp3":
        messagebox.showerror(title="Unsupported Format",message="Please choose an mp3 file")
        print("Unsupported format")
        return False
    else:return True

