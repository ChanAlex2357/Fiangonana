from datetime import date , datetime , timedelta
from models.alahady import Alahady
from helpers.database import DataAccess
from decimal import Decimal

# recuperer la derniere date de pret soit la date a la quelle la caisse est dispo
def get_date_dispo():
    # Connexion database "Fiangonana"
    conn = DataAccess.getFiangonanaConnection()
    cursor = conn.cursor()

    cursor.execute("select date_pret_valide from Caisse")
    row = cursor.fetchone()
    conn.close()

    if row.date_pret_valide == None:
        date_dispo = datetime.now()
    else :
        date_dispo = datetime.strptime(row.date_pret_valide,'%Y-%m-%d')

    if date_dispo.date() <= datetime.now().date():
        date_dispo = Alahady.get_closest_alahady()
    try :
        curr = Alahady(date_reel=date_dispo.date())
    except Exception :
        curr =  Alahady.get_closest_alahady()
    curr.next()
    return curr

def get_montant():
    # Connexion database Fiangonana
    conn = DataAccess.getFiangonanaConnection()
    cursor = conn.cursor()
    
    cursor.execute("select montant_actuelle from Caisse")
    row = cursor.fetchone()
    montant = Decimal(row.montant_actuelle)
    if montant < 0 :
        montant = 0
    return montant
def update_value( value):
    conn = DataAccess.getFiangonanaConnection()
    cursor = conn.cursor()
    

def update_date(date_valide):
    conn = DataAccess.getFiangonanaConnection()
    cursor = conn.cursor()
    print(date_valide)
    try :
        
        conn.commit()
    except Exception:
        conn.rollback()
    finally :
        conn.close()
