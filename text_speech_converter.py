#Downloading libraries
pip install tkinter
pip install gTTS
pip install playsound

#Importing libraries
from  tkinter import *
from gtts import gTTS
from playsound import playsound

#Initializing window
geometry root.("350x300") 
root.configure(bg='ghost white')
root.title("TEXT TO SPEECH CONVERTER")

Label(root, text = "TEXT TO SPEECH", font = "arial 20 bold", bg='white smoke').pack()
Label(text ="Conveter", font = 'arial 15 bold', bg ='white smoke' , width = '20').pack(side = 'bottom')
Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)

#Funtion to convert Text to Speech

def Text_to_Speech:
  Message = entry_field.get()
  speech = gTTS(text = Message)
  speech.save('Converted.mp3')
  playsound('Conerted.mp3')
