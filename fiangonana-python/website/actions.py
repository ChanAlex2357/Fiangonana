from flask import Blueprint , render_template , request , redirect ,session
from models.mpino import Mpino
from helpers import dates
from models.pret import Pret

actions = Blueprint('actions' , __name__)

@actions.route('valider-pret' , methods=['GET' , 'POST'])
def valider():
    id_mpino = 0 
    if request.method == 'POST':
        date_pret = request.form.get('datePret')
        montant = request.form.get('montant')
        mpino = request.form.get('idMpino')
        
        id_mpino = mpino
        Pret(0,date_pret,montant,mpino).valider()
    return redirect(f"/pret-demande/{id_mpino}")