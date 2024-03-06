from datetime import date , datetime , timedelta
from models.alahady import Alahady
from helpers.database import DataAccess

# recuperer la derniere date de pret soit la date a la quelle la caisse est dispo
def get_date_dispo():
    # Connexion database "Fiangonana"
    conn = DataAccess.getFiangonanaConnection()
    cursor = conn.cursor()

    cursor.execute("select date_dispo from v_caisse")
    row = cursor.fetchone()

    date_dispo = datetime.strptime(row.date_dispo,'%Y-%m-%d')
    if date_dispo.date() < datetime.now().date():
        date_dispo = Alahady.get_closest_alahady()

    curr = Alahady(date_reel=date_dispo.date())
    curr.next()
    return curr

def get_montant():
    # Connexion database Fiangonana
    conn = DataAccess.getFiangonanaConnection()
    cursor = conn.cursor()
    
    cursor.execute("select montant_actuelle from v_caisse")
    row = cursor.fetchone()

    montant = int(row.montant_actuelle)
    if montant < 0 :
        montant = 0 
    return montant