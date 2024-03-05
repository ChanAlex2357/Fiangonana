from tkinter import *
from ttkbootstrap import *
import ttkbootstrap as ttb
from ttkbootstrap.constants import *
from .constantes import *
from gui import app

# Frame content
body = ttb.Frame(app,bootstyle="primary" , width=BODY_WIDTH, height= BODY_HEIGHT)
body.grid(column=0,row=1)