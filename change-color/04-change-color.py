from tkinter import*
from tkinter import font
from define import *

from app import App

window = Tk()

app = App(window)

def change_label(bground):
    labelTitle['bg']=bground

def creat_btn(name,bground,index):
    Button(window, text=name, font=font_Text, bg=bground, fg=COLOR_BLACK, padx=10, pady=5, command=lambda:change_label(bground) ).grid(row=1, column=index,sticky=W+E,padx=20)

font_Title = font.Font(family = "Stencil Std", size=20)
font_Text = font.Font(family = "Terminal", size=20)

labelTitle = Label(window, text="Hello", font=font_Title, bg=COLOR_YELLOW, fg=COLOR_BLACK, width=5, padx=10, pady=20 )
labelTitle.grid(row=0, column=0, columnspan=4,sticky="wse")

creat_btn("Green",COLOR_GREEN,0)
creat_btn("Blue",COLOR_BLUE,1)
creat_btn("Red",COLOR_RED,2)
creat_btn("Yellow",COLOR_YELLOW,3)

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.columnconfigure(3,weight=1)


window.mainloop()
