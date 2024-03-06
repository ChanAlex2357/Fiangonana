from tkinter import *
from ttkbootstrap import *
import ttkbootstrap as ttb
from .constantes import *

app = ttb.Window(themename="superhero")
app.title("Fiangonana")
app.geometry(WINDOW_SIZE)

from .views.rakitra import RakitraView

def run():
    rv = RakitraView()
    # rv.set_layout_config()
    
    from .navbar import navbar
    from .body import body
    app.mainloop()
