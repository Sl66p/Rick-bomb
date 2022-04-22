from tkinter import *
from tkinter import messagebox
import webbrowser

# Variables
RollLink = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
loop = 1

# RollLoop
while loop > 0:
      webbrowser.open_new(RollLink)
      messagebox.askretrycancel("Sl66p x ColDog", "Get Rolled!")
      loop += 1