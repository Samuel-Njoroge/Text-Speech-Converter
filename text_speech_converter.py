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

def Text_to_Speech():
  Message = entry_field.get()
  speech = gTTS(text = Message)
  speech.save('Converted.mp3')
  playsound('Converted.mp3')
  
#Exit function
def Exit():
  root.destroy()
  
 #Reset function
def Reset():
  Msg.set("")
  
 #Defining buttons
Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)

Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)

Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset).place(x=175 , y = 140)

#Executing and running the program
root.mainloop()
