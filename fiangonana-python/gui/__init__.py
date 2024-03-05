from tkinter import *
from ttkbootstrap import *
import ttkbootstrap as ttb
from .constantes import *

app = ttb.Window(themename="superhero")
app.title("Fiangonana")
app.geometry(WINDOW_SIZE)

def run():
    from .body import body
    from .navbar import navbar
    app.mainloop()
