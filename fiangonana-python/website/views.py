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

@views.route('rakitra-insertion' , methods = ['GET' , 'POST'])
def rakitra_insertion():
    if request.method == 'POST':
        date_demande = request.form.get('dateDepot')
        montant = request.form.get('montant')
        state = Rakitra(0,date_demande , montant).save()
        if state == False :
            return redirect("/")
    return render_template("rakitra-insertion.html")

@views.route('mpino-login', methods=['GET','POST'])
def mpino_login():
    if request.method == 'GET':
        return render_template("mpino-login.html")
    elif request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        
        auth = Mpino.authentification(login=login , password=password)
        if auth :
            return redirect(f"/pret-demande/{auth.get_id_mpino()}")
        else :
            return render_template("mpino-login.html")
    

@views.route('pret-demande/<int:id_mpino>' , methods=['GET','POST'])
def demander_pret(id_mpino):
    if id_mpino <= 0 :
        return redirect("/mpino-login")
    if request.method == 'GET':
        return render_template("pret-demande.html" , id_mpino = id_mpino)
    elif request.method == 'POST':
        date_demande = request.form.get('dateDemande')
        montant = request.form.get('montant')
        mpino = request.form.get('idMpino')
        # Calcule de la date
        pr = Pret.demander_pret(int(mpino),dates.string_to_date(date_demande),float(montant))
        return render_template("pret-validation.html",pret=pr)