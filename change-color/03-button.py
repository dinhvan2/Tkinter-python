from tkinter import*
from tkinter import font
from define import *

from app import App

window = Tk()

app = App(window)

def show_info(name):
    print(name)
font_Title = font.Font(family = "Stencil Std", size=20)
font_Text = font.Font(family = "Terminal", size=20)
# label
labelTitle = Button(window, text="Hello", font=font_Text, bg=COLOR_YELLOW, fg=COLOR_BLACK, padx=10, pady=5 )
labelTitle.grid(row=0, column=0)

labelPython = Button(window, text="Python", font=font_Text, bg=COLOR_RED, fg=COLOR_BLACK, padx=10, pady=5, command=lambda:show_info("python") )
labelPython.grid(row=0, column=1)

labelTkinter = Button(window, text="Tkinter", font=font_Text, bg=COLOR_GREEN, fg=COLOR_BLACK, padx=10, pady=5 )
labelTkinter.grid(row=0, column=2)


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

window.mainloop()
