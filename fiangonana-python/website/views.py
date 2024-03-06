from flask import Blueprint , render_template , request , redirect ,session
from models.mpino import Mpino
from helpers import dates
from models.pret import Pret
from models.rakitra import Rakitra

views = Blueprint('views' , __name__)


# Mapping d'un URL avec une fonction a executer
@views.route('/')
def home():
    return render_template("home.html")

@views.route('mpino-login', methods=['GET','POST'])
def mpino_login():
    if request.method == 'GET':
        return render_template("mpino-login.html")
    elif request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        
        auth = Mpino.authentification(login=login , password=password)
        if auth :
            return redirect(f"/pret/demande/{auth.get_id_mpino()}")
        else :
            return render_template("mpino-login.html")
    

