from helpers.database import DataAccess
import pyodbc
class Mpino :
	def __init__(self,id_mpino,nom,login,password):
		self.set_id_mpino(id_mpino)
		self.set_nom(nom)
		self.set_login(login)
		self.set_password(password)
#Getteurs and Setteurs
	#id_mpino
	def get_id_mpino(self):
		return self._id_mpino

	def set_id_mpino(self,id_mpino):
		self._id_mpino=id_mpino

	#nom
	def get_nom(self):
		return self._nom

	def set_nom(self,nom):
		self._nom=nom

	#login
	def get_login(self):
		return self._login

	def set_login(self,login):
		self._login=login

	#password
	def get_password(self):
		return self._password

	def set_password(self,password):
		self._password=password

	def authentification(login , password):
		result = None
  		# Connexion a la base de donnee
		conn = DataAccess.getFiangonanaConnection()
		cursor = conn.cursor()
		sql = "select * from Mpino where login = ? AND password = ?"
		try :
			cursor.execute(sql,(login,password))
			row = cursor.fetchone()
			if row != None:
				result = Mpino(row.idMpino , row.nomMpino , row.login , row.password)
		except pyodbc.Error as err:
			print(err)
		finally :
			conn.close()
		return result
		
		