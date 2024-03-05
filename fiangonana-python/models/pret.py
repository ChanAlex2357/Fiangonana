from datetime import date , datetime , timedelta
from models.alahady import Alahady
from models.rakitra import Rakitra
from models import caisse
import math
class Pret :
	def __init__(self,id_pret,date_pret,montant,id_mpino):
		self.set_id_pret(id_pret)
		self.set_date_pret(date_pret)
		self.set_montant(montant)
		self.set_id_mpino(id_mpino)
#Getteurs and Setteurs
	#id_pret
	def get_id_pret(self):
		return self._id_pret

	def set_id_pret(self,id_pret):
		self._id_pret=id_pret

	#date_pret
	def get_date_pret(self):
		return self._date_pret

	def set_date_pret(self,date_pret):
		self._date_pret=date_pret

	#montant
	def get_montant(self):
		return self._montant

	def set_montant(self,montant):
		self._montant=montant

	#id_mpino
	def get_id_mpino(self):
		return self._id_mpino

	def set_id_mpino(self,id_mpino):
		self._id_mpino=id_mpino

# Functionalities
	def get_intervalle_debut(current_dimanche):
		# numero de la date de demande
		id_demande = Alahady.get_id_dimanche_by_date(current_dimanche.get_date_reel())
		intervalle = []
		if id_demande >= 1 :
			for i in range(1,id_demande+1):
				intervalle.append(i)
		return intervalle

	def calcule_pourcentage( rakitra_annee : list , rakitra_ref : list , intervalle : list):
		# les rakitra utils pour le pourcentage
		pourcent_current = rakitra_annee[:len(intervalle)]
		pourcent_ref = rakitra_ref[:len(intervalle)]
		# Calcul des 2 sommes
		sum_current = 0
		sum_ref = 0
		for i in range(len(intervalle)):
			sum_current += pourcent_current[i].get_montant()
			sum_ref += pourcent_ref[i].get_montant()
		percent = (sum_current / sum_ref )
		return percent

	def calcul_prevision(rakitra_ref,dimanche:Alahady , poucentage):
		id_dim = dimanche.get_id_dimanche()
		ref_value = rakitra_ref[id_dim-1]
		result = ref_value.get_montant()*poucentage
		return result

	def get_date_pret_valide(rakitra_annee ,rakitra_ref,date_base ,montant_depart,montant_final,poucentage):
		total = montant_depart
		while(total < montant_final):
			mnt = Pret.calcul_prevision(rakitra_ref,date_base,poucentage)
			total += mnt
			date_base.next()
		date_base.previous()
	
	def demander_pret(date_demande : date , montant):
		year = date_demande.year
		current_dimanche = Alahady.get_closest_alahady(date_base=date_demande)

		# Recuperer l'intervalle depuis debut de l'annee
		intervalle = Pret.get_intervalle_debut(current_dimanche)

		# Recuperer les rakitra des annees utils
		rakitra_annee = Rakitra.get_all_rakitra_of_year(year)
		rakitra_ref = Rakitra.get_all_rakitra_of_year(year-1)

		# Calcul du pourcentage
		poucentage = Pret.calcule_pourcentage(rakitra_annee , rakitra_ref , intervalle)
		temp_somme = caisse.get_montant()

  		# Calcul des previsions
		current_dimanche.next()
		Pret.get_date_pret_valide(rakitra_annee,rakitra_ref,current_dimanche,temp_somme,montant,poucentage)

		return current_dimanche