# ColDog Studios x Sl66p Rick Bomb
# Last Modified: 4/21/22

from tkinter import *
from tkinter import messagebox
import webbrowser

# Variables
RollLink = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
loop = 1

# RollLoop
while loop > 0:
      webbrowser.open_new(RollLink)
      messagebox.askretrycancel("ColDog Studios x Sl66p", "Get Rolled!")
      