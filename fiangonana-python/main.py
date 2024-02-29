from models import Alahady
from datetime import datetime , date
def main():
    print("\nBonjour ce programme est destiner pour projet S4 n_1 \nElle consiste a realiser un systeme qui fait la suggstion de pret financier au pret d'une eglise connecter\n")
    # array = Alahady.Alahady.get_all_date_dimanche_of(2023)
    # for i in range(0 , len(array)):
    #     print(array[i].to_string())
    
    print(Alahady.Alahady.get_id_dimanche_by_date( ddate= date(2024,3,13)))
main()