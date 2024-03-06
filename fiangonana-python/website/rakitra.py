from flask import Blueprint , render_template , request , redirect ,session
from models.mpino import Mpino
from helpers import dates
from models.pret import Pret
from models.rakitra import Rakitra

rakitra = Blueprint('rakitra' , __name__)

@rakitra.route('insertion' , methods = ['GET' , 'POST'])
def rakitra_insertion():
    if request.method == 'POST':
        date_demande = request.form.get('dateDepot')
        montant = request.form.get('montant')
        state = Rakitra(0,date_demande , montant).save()
        if state == False :
            return redirect("/")
    return render_template("rakitra-insertion.html")