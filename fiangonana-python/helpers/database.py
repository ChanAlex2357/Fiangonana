import pyodbc
class DataAccess :
	def __init__(self,driver_name,server_name,database_name,username,password):
		self.setDriver_name(driver_name)
		self.setServer_name(server_name)
		self.setDatabase_name(database_name)
		self.setUsername(username)
		self.setPassword(password)

	def __init__ (self,database_name):
		self.setDatabase_name(database_name)
#Getteurs and Setteurs
	#driver_name
	def getDriver_name(self):
		return self._driver_name

	def setDriver_name(self,driver_name):
		self._driver_name=driver_name

	#server_name
	def getServer_name(self):
		return self._server_name

	def setServer_name(self,server_name):
		self._server_name=server_name

	#database_name
	def getDatabase_name(self):
		return self._database_name

	def setDatabase_name(self,database_name):
		self._database_name=database_name

	#username
	def getUsername(self):
		return self._username

	def setUsername(self,username):
		self._username=username

	#password
	def getPassword(self):
		return self._password

	def setPassword(self,password):
		self._password=password

	def getUrlConnection(self):
		return 'DRIVER={SQL Server};'f"SERVER=DESKTOP-JCA;DATABASE={self.getDatabase_name()};Trusted_Connection=yes;username=DESKTOP-JCA\JACQUES Chan;password="

	def getConnection(self):
		data = pyodbc.connect(self.getUrlConnection())
		return data
	def getFiangonanaConnection():
		db = DataAccess("Fiangonana")
		return db.getConnection()