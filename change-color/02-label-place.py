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
labelTitle.place(relx = 0.5,rely = 0.5, anchor= CENTER)



window.mainloop()
