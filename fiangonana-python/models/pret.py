from datetime import date , datetime , timedelta
from models.alahady import Alahady
from models.rakitra import Rakitra
from models import caisse
import pyodbc
from helpers import dates , database as db

import math
class Pret :
	def __init__(self,id_pret : None , date_pret : [str,date],montant,id_mpino : int):
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

	def set_date_pret(self,date_pret : [str,date]):
		dd = date_pret
		try :
			dd = dates.string_to_date(date_pret)
			print("transfo")
		except Exception as e:
			print(e)
			print("Date pret is not a String")
		self._date_pret=dd

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

	def show(self):
		print(f"[{self.get_id_pret()}] {self.get_date_pret()} ~ {self.get_montant()}")
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
		year = dimanche.get_annee()
		year_ref = year - 1
		id_dim = dimanche.get_id_dimanche()
		# Recuperer le rakitra reference
		rk_ref = Rakitra.get_rakitra_of(id_dim,year_ref)
		ref_value = 0
		# y a pas de ref => atao prevision sinon montant de ref = montant
		if rk_ref.get_id_rakitra() == 0:
      
			al_ref = Alahady(date_reel=rk_ref.get_date_depot())
			ref_value = Pret.calcul_prevision(rakitra_ref,al_ref,poucentage)
		else :
			ref_value = rk_ref.get_montant()
		result = ref_value*poucentage
		return result

	def get_date_pret_valide(rakitra_annee ,rakitra_ref,date_base ,montant_depart,montant_final,poucentage):
		total = montant_depart
		year = date_base.get_annee()
		while(total < montant_final):
			date_base.show()
			mnt = Pret.calcul_prevision(rakitra_ref,date_base,poucentage)
			rk = Rakitra(0,date_depot=date_base.get_date_reel() , montant=mnt)
			rk.show()
			rakitra_annee.append( rk )
			total += mnt
			date_base.next()
		date_base.previous()

	
	def demander_pret( id_mpino ,date_demande : date , montant):
		year = date_demande.year
		current_dimanche = Alahady.get_closest_alahady(date_base=date_demande)
		current_dimanche.show()
		# Recuperer l'intervalle depuis debut de l'annee
		intervalle = Pret.get_intervalle_debut(current_dimanche)

		# Recuperer les rakitra des annees utils
		rakitra_annee = Rakitra.get_all_rakitra_of_year(year)
		rakitra_ref = Rakitra.get_all_rakitra_of_year(year-1)

		# Calcul du pourcentage
		poucentage = Pret.calcule_pourcentage(rakitra_annee , rakitra_ref , intervalle)
		temp_somme = caisse.get_montant()
		print(f"poucentage == {poucentage}")
		if temp_somme < montant :
			current_dimanche = caisse.get_date_dispo()
			# Calcul des previsions
			Pret.get_date_pret_valide(rakitra_annee,rakitra_ref,current_dimanche,temp_somme,montant,poucentage)
		else :
			current_dimanche.next()
		result = Pret( id_pret=0 , date_pret=current_dimanche.get_date_reel() , montant=montant , id_mpino=id_mpino)
		return result

	def valider(self):
		# connexion base de donner Fiangonana
		fiangoana_db = db.DataAccess("Fiangonana")
		sql = f"Insert into Pret(datePret,montant,idMpino) values ('{self.get_date_pret()}' , {self.get_montant()} , {self.get_id_mpino()})"
		# Execution du sql
		conn = fiangoana_db.getConnection()
		cursor = conn.cursor()
		try :
			cursor.execute(sql)
			conn.commit()
		except pyodbc.Error:
			conn.rolleback()
		finally :
			conn.close()