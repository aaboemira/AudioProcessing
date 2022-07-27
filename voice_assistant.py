from neuralintents import GenericAssistant
import speech_recognition as sr
import pyttsx3 as tts
import webbrowser
import sys

recog = sr.Recognizer()
speaker = tts.init()
speaker.setProperty('rate', 150)
voices = speaker.getProperty('voices')
speaker.setProperty('voice', voices[1].id)

todo_list = ['Go Shopping', 'Clean Room', 'Record Video']

def speaker_say(speaker, message):
    speaker.say(message)
    speaker.runAndWait()

def text_recognized(recognizer):
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recog.listen(mic)
        recognized = recog.recognize_google(audio)
        return recognized.lower()


def create_note():
    global recog, speaker
    speaker_say(speaker, 'What do you want to write onto your note?')
    
    done = False
    while not done:
        try:
            note = text_recognized(recog)
            speaker_say(speaker, "Choose a file name!")
            file_name = text_recognized(recog)
            with open(f"{file_name}.txt", 'w') as f:
                f.write(note)
                done = True
                speaker_say(speaker, f"I successfully created the note {file_name} for you")
        except sr.UnknownValueError:
            recog = sr.Recognizer()
            speaker_say(speaker, "I didn't get that! please try again.")

def add_todo():
    global recog, speaker
    speaker_say(speaker, "What to do you want to add?")
    done = False
    while not done:
        try:
            item = text_recognized(recog)
            todo_list.append(item)
            done = True
            speaker_say(speaker, f"I added {item} to the to do list")
        except sr.UnknownValueError:
            recog = sr.Recognizer()
            speaker_say(speaker, "I didn't get that! please try again.")

def show_todos():
    global speaker
    speaker_say(speaker, "The items on your to do list are the following")
    for item in todo_list:
        speaker.say(item)
    speaker.runAndWait()

def search():
    global speaker, recog
    speaker_say(speaker, "What do you want to search for?")
    done = False
    while not done:
        try:
            keyword = text_recognized(recog)
            speaker_say(speaker, f"Here is what I found on google for {keyword}")
            webbrowser.get().open(f"https://google.com/search?q={keyword}")
            done = True
        except sr.UnknownValueError:
            recog = sr.Recognizer()
            speaker_say(speaker, "I didn't get that! please try again.")

def hello():
    global speaker
    speaker_say(speaker, "hi sir, How can I help you?")

def name():
    global speaker
    speaker_say(speaker, "My name is Bless")

def quit():
    global speaker
    speaker_say(speaker, "Bye")
    sys.exit(0)

mappings = {
    "greeting": hello,
    "name": name,
    "create_note": create_note,
    "add_todo": add_todo,
    "show_todos": show_todos,
    "quit": quit,
    "search": search
}

assistant = GenericAssistant('intents.json', intent_methods=mappings)
# assistant.train_model()
# assistant.save_model("voice_assistant_version2")
assistant.load_model("voice_assistant_version2")

while True:
    try:
        message = text_recognized(recog)
        assistant.request(message)
    except sr.UnknownValueError:
        recog = sr.Recognizer()