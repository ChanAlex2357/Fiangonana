import gui
from models.pret import Pret
from helpers import dates
def main():
    # print("\nBonjour ce programme est destiner pour projet S4 n_1 \nElle consiste a realiser un systeme qui fait la suggstion de pret financier au pret d'une eglise connecter\n")
    p = Pret.demander_pret(1, dates.string_to_date("2024-03-06") ,1000000 )
    p.show()
main()