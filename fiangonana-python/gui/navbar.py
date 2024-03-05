from tkinter import *
from ttkbootstrap import *
import ttkbootstrap as ttb
from ttkbootstrap.constants import *
from .constantes import *
from gui import app

# Frame navbar
navbar = ttb.Frame( app ,bootstyle="dark",height=NAVBAR_HEIGHT , width=NAVBAR_WIDTH)
navbar.grid(column=0 , row=0)

## Navbar links
__rakitra_link = ttb.Button( navbar,text="Insertion rakitra",bootstyle="light")
__rakitra_link.grid(column=1 , row=0 , pady=10 , padx=5)

__pret_link = ttb.Button( navbar,text="Demander un pret",bootstyle="light" )
__pret_link.grid(column=0 , row=0 , pady=10 , padx=5)