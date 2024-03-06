from helpers.database import DataAccess as db
import pyodbc
from datetime import date , datetime , timedelta
import models.alahady as m_alahady

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
		rakitra = Rakitra()
		date_rk = m_alahady.Alahady.get_date_dimanche_of(id_dimanche,year)

		# connexion base de donner Fiangonana
		fiangoana_db = db.DataAccess("Fiangonana")

		# Execution du sql
		conn = fiangoana_db.getConnection()
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