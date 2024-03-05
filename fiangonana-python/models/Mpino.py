from helpers.database import DataAccess
class Mpino :
	def __init__(self	,nom	,login	,password):
		self.setNom(nom)
		self.setLogin(login)
		self.setPassword(password)
#Getteurs and Setteurs
	#nom
	def getNom():
		return self._nom

	def setNom(self,nom):
		self._nom=nom

	#login
	def getLogin():
		return self._login

	def setLogin(self,login):
		self._login=login

	#password
	def getPassword():
		return self._password

	def setPassword(self,password):
		self._password=password

	def authentification(login , password):
		# Connexion a la base de donnee
		conn = DataAccess.getFiangonanaConnection()
		cursor = conn.cursor()
		sql = "select * from Mpino where login = ? AND password = ?"

		cursor.execute(sql,(login,password))
		row = cursor.fetchone()
		