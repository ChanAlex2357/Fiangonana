select AVG(variation) as moyenne_variation from
(select tb1.numSemaine,moyenne , montant , montant/moyenne as variation
from (select numSemaine , montant From Rakitra where annee = 2024 ) as tb1 
join (select numSemaine , AVG(montant) as moyenne from Rakitra where (annee = 2022 OR annee = 2023)  group by numSemaine) as tb2 on tb1.numSemaine = tb2.numSemaine) as tb