from re import A
from ssl import AlertDescription
from tkinter.messagebox import YES, showinfo
from turtle import goto
from tkinter import *
from tkinter import messagebox
import webbrowser
import ctypes  # An included library with Python install, draws boxes, makes alert screens

# Rickroll Link :)
RollLink = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"

# Draw an Alert Box, with options
##  Styles:
##  0 : OK
##  1 : OK | Cancel
##  2 : Abort | Retry | Ignore
##  3 : Yes | No | Cancel
##  4 : Yes | No
##  5 : Retry | Cancel 
##  6 : Cancel | Try Again | Continue

# Code to draw the box
# def Mbox(title, text, style):
  # return ctypes.windll.user32.MessageBoxW(0, text, title, style)
# Mbox('Your title', 'Your text', 1)

#def Mbox(title, text, style):
#    return ctypes.windll.user32.MessageBoxW(0, text, title, 0)
#Mbox('Get Rolled!', 'Prepare to be Rolled!', 0)

#if Mbox == 0:
     # goto loop




loop = 1

while loop > 0:
      webbrowser.open_new(RollLink)
      messagebox.askretrycancel("askretrycancel", "Get Rolled!")
      
      loop += 1