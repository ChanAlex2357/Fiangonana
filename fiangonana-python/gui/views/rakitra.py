from .__view__ import View
from tkinter import *
from ttkbootstrap import *
import ttkbootstrap as ttb
from ttkbootstrap.constants import *
from gui.constantes import *
from gui.body import body

class RakitraView(View):
    def __init__(self):
        self.instance = ttb.Frame(body,width=MAX_WIDTH , height=100 , bootstyle="danger")

    def set_layout_config(self):
        self.instance.grid(column=0,row=1)

    def remove_layout(self):
        self.instance.grid_remove()