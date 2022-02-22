from tkinter import *
from django.template import engines
 
import pyttsx3

engine = pyttsx3.init()
engine.say('I am Alfred Owino And this is what i want to do for all my life')

engine.runAndWait()