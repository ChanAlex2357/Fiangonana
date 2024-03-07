from helpers.database import DataAccess as db
import pyodbc
from datetime import date , datetime , timedelta
from .alahady import Alahady

class Rakitra :
	def __init__(self,id_rakitra = None, date_depot = None ,montant = None):
		self.set_id_rakitra(id_rakitra)
		self.set_date_depot(date_depot)
		self.set_montant(montant) 
	def show(self):
		print(f"Rakitra n_{self.get_id_rakitra()} : {self.get_montant()} [{self.get_date_depot()}]")
#Getteurs and Setteurs
	#id_rakitra
	def get_id_rakitra(self):
		return self._id_rakitra

	def set_id_rakitra(self,id_rakitra):
		self._id_rakitra=id_rakitra

	#date_depot
	def get_date_depot(self):
		return self._date_depot

	def set_date_depot(self,date_depot):
		self._date_depot=date_depot

	#montant
	def get_montant(self):
		return self._montant

	def set_montant(self,montant):
		self._montant=montant


#   Functionalities
	# recuperer la liste des rakitra dans une annee specifier 
	def get_by_row(row):
		date_row = datetime.strptime(row.dateDepot,'%Y-%m-%d')
		rk = Rakitra(row.idRakitra , date_row.date() , row.montant)
		return rk

	def get_all_rakitra_of_year(year):
		list_rakitra = list()
		# connexion base de donner Fiangonana
		
		sql = "select * from Rakitra Where YEAR(dateDepot) = ? order by dateDepot"

		# Execution du sql
		conn = db.getFiangonanaConnection()
		cursor = conn.cursor()
		try :
			cursor.execute(sql , year)
			rows = cursor.fetchall()
			for row in rows:
				rk = Rakitra.get_by_row(row)
				list_rakitra.append(rk)
		except pyodbc.Error as err:
			print("Cannot get the list of Rakitra")
		finally :
			cursor.close()
			conn.close()

		return list_rakitra
	# Recuperer le rakitra selon un nemero et une date donnee
	def get_rakitra_of( id_dimanche , year):
		date_rk = Alahady.get_date_dimanche_of(id_dimanche,year)
		rakitra = Rakitra(0,date_rk,0)
		# Execution du sql
		conn = db.getFiangonanaConnection()
		cursor = conn.cursor()
		try :
			cursor.execute("select * from Rakitra Where dateDepot=?", (date_rk.strftime("%Y-%m-%d"),))
			row = cursor.fetchone()
			if row :
				rakitra = Rakitra.get_by_row(row)
		except pyodbc.Error as err:
			print(err)
			print(f"Impossible de recuperer le rakitra correspondant a date '{date_rk}' as [{id_dimanche};{year}]")
		finally :
			cursor.close()
			conn.close()
		return rakitra

	def save(self):
		boolean = False
		# Execution du sql
		conn = db.getFiangonanaConnection()
		cursor = conn.cursor()
		try :
			cursor.execute(f"insert into Rakitra (montant,dateDepot) values(?,?)" , [(self.get_montant()),(self.get_date_depot()),])
			conn.commit()
			boolean = True
		except pyodbc.Error as err:
			print(err)
			conn.rollback()
		finally :
			conn.close()
		return boolean

	def get_moyenne_predictive(id_dimanche : int , annee : int):
		annee_1 = annee - 1
		annee_2 = annee - 2
		result = 0
		sql = "select AVG(montant) as moyenne from Rakitra where (annee = ? OR annee = ?) AND (numSemaine = ?)  group by numSemaine"
  
		conn = db.getFiangonanaConnection()
		cursor = conn.cursor()
		try :
			cursor.execute(sql , [(annee_1),(annee_2),(id_dimanche),])
			row = cursor.fetchone()	
			result = row.moyenne
		except pyodbc.Error as err:
			print(err)
			conn.rollback()
		finally :
			conn.close()
		return result
  
	def get_moyenne_variation(annee : int):
		annee_1 = annee - 1
		annee_2 = annee - 2
		result = 0
		sql = "select AVG(variation) as moyenne_variation from (select tb1.numSemaine,moyenne , montant , montant/moyenne as variation from (select numSemaine , montant From Rakitra where annee = ? ) as tb1  join (select numSemaine , AVG(montant) as moyenne from Rakitra where (annee = ? OR annee = ?)  group by numSemaine) as tb2 on tb1.numSemaine = tb2.numSemaine) as tb"
		
		conn = db.getFiangonanaConnection()
		cursor = conn.cursor()
		try :
			cursor.execute(sql , [(annee),(annee_1),(annee_2),])
			row = cursor.fetchone()	
			result = row.moyenne_variation
		except pyodbc.Error as err:
			print(err)
			conn.rollback()
		finally :
			conn.close()
		return result
  