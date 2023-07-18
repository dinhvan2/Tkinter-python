from tkinter import *
from define import *
import os
root = Tk()
 
def setup_window():
    # set width and height, position
    root.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_POSITION_RIGHT,WINDOW_POSITION_DOWN)) 

    # set title
    root.title("Dinh Van")

    # set icon
    root.iconbitmap(os.path.join(PATH_IMAGES,'icon.ico'))

    #set background
    root['bg'] = COLOR_BG

    root.resizable(False,False)
setup_window()
root.mainloop()