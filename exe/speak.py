from logging import root
from tkinter import *
from django.template import engines
 
import pyttsx3

root =Tk()

root.title("Alfred's Text to Speach")
root.geometry('800x500')


def talk():
    engine = pyttsx3.init()
    rate = engine.getProperty('rate')   
    engine.setProperty('rate', 100)
    voices = engine.getProperty('voices')  
    engine.setProperty('voice', voices[0].id)
    engine.say(myenstry.get())
    engine.runAndWait()
    myenstry.delete(0, END)
    

myenstry = Entry(root, font=('Monaco', 28))
myenstry.pack(pady=20)


mybutton = Button(root, text = 'speak', command=talk)
mybutton.pack(pady=20)  


root.mainloop()