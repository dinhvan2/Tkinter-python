from define import *
import os
class App():
    def __init__(self,window) -> None:
        # set width and height, position
        window.geometry("{}x{}+{}+{}".format(WINDOW_WIDTH,WINDOW_HEIGHT,WINDOW_POSITION_RIGHT,WINDOW_POSITION_DOWN)) 

        # set title
        window.title("Dinh Van")

        # set icon
        window.iconbitmap(os.path.join(PATH_IMAGES,'icon.ico'))

        #set background
        window['bg'] = COLOR_BG

        window.resizable(False,False)