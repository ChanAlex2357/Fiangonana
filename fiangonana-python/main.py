import gui
from models.pret import Pret
from helpers import dates
from models.alahady import Alahady
from models.rakitra import Rakitra
import models.caisse as Caisse
def main():
    # print("\nBonjour ce programme est destiner pour projet S4 n_1 \nElle consiste a realiser un systeme qui fait la suggstion de pret financier au pret d'une eglise connecter\n")
    p = Pret.demander_pret(1, None ,55000000)
main()