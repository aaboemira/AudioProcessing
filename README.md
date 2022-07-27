Audio Processing project
GUI application for processing audio files 
Langeuages used:
Python 310

##Modules Used
1- sys
2- Sounddevice
3- Matplotlib
4- speechrecognition
5- Pydub
6- Tkinter
7- Soundfile
8- pyrubberband

Install guide:
Download libraries:
	open the terminal and type: pip install <module_name>
For pyrubberband:
	1 Download rubberband library cli from here(https://breakfastquay.com/rubberband/) ( folder containing rubberband.exe and libsndfile-1.dll)
	2 Go to Windows System Environment and Add the folder to Path
	3 Create System Variable with Variable name "rubberband" and path to the rubberband.exe
	4 Make sure all your relevant users can access the path and the rubberband variable.This can be checked by opening cmd and typing "rubberband". If the command works, the library is recognized.
	5. Restart the Program in which you want to access the library 

For pydub:
	1-Download ffmpeg from official website 
	2-Go to Windows System Environment and Add the bin folder to Path
	3-Do pip install ffmpeg and then you will be able to use it without any problems.
