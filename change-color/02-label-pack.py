from tkinter import*
from tkinter import font
from define import *

from app import App

window = Tk()

app = App(window)

font_Title = font.Font(family = "Stencil Std", size=44, weight = font.BOLD)
font_Text = font.Font(family = "Terminal", size=20)
# label
labelTitle = Label(window, text="Hello", font=font_Title, bg=COLOR_RED, fg=COLOR_YELLOW, width=5, padx=10, pady=20 )
labelTitle.pack(side=LEFT, anchor= NW)

labelText = Label(window, text="Welcom to my page", font=font_Text, bg=COLOR_RED, fg=COLOR_YELLOW, width=10, padx=40, pady=20 )
labelText.pack(side=RIGHT, anchor= SE)

window.mainloop()
