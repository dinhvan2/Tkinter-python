from tkinter import*
from tkinter import font
from define import *

from app import App

window = Tk()

app = App(window)

font_Title = font.Font(family = "Stencil Std", size=20)
font_Text = font.Font(family = "Terminal", size=20)
# label
labelTitle = Label(window, text="Hello", font=font_Text, bg=COLOR_RED, fg=COLOR_YELLOW, padx=10, pady=5 )
labelTitle.grid(row=0, column=0)

labelText = Label(window, text="Welcom", font=font_Text, bg=COLOR_BLUE, fg=COLOR_YELLOW, padx=10, pady=5 )
labelText.grid(row=0, column=1)

labelText = Label(window, text="Mypage", font=font_Text, bg=COLOR_GREEN, fg=COLOR_YELLOW, padx=10, pady=5 )
labelText.grid(row=0, column=2)

window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)

window.mainloop()
