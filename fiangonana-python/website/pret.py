from flask import Blueprint , render_template , request , redirect ,session
from models.mpino import Mpino
from helpers import dates
from models.pret import Pret
from models.rakitra import Rakitra

pret = Blueprint('pret' , __name__)

@pret.route('demande/<int:id_mpino>' , methods=['GET','POST'])
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