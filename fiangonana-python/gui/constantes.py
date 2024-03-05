from tkinter import *
from ttkbootstrap import *
import ttkbootstrap as ttb
from ttkbootstrap.constants import *
MAX_WIDTH = 1080
MAX_HEIGHT = 720
WINDOW_SIZE = f"{MAX_WIDTH}x{MAX_HEIGHT}"

# NAVBAR
NAVBAR_WIDTH = MAX_WIDTH
NAVBAR_HEIGHT = 70

## NAV_LINK
def NAV_LINK( master , text , bootstyle):
    return ttb.Button( master=master,text=text,bootstyle=bootstyle ,height=30)

# BODY
BODY_WIDTH = MAX_WIDTH
BODY_HEIGHT = MAX_HEIGHT - NAVBAR_HEIGHT