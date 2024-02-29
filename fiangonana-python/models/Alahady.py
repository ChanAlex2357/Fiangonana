from datetime import date , timedelta , datetime
class Alahady :
	def __init__(self,date_reel=None ,id_dimanche=None,annee=None):
		self.set_id_dimanche(id_dimanche)
		if (annee == None) and (date_reel != null) :
			annee = date_reel.year
		self.set_annee(annee)
		self.set_date_reel(date_reel)

#Getteurs and Setteurs
	#date_reel
	def get_date_reel(self):
		return self._date_reel

	def set_date_reel(self,date_reel):
		if( date_reel == None ):
			try :
				date_reel = ( Alahady.get_date_dimanche_of( self.get_id_dimanche() , self.get_annee() ) )
			except:
				print("Il n'y a pas de donnee suffisante pour etablir le parametre de date ")
		self._date_reel=date_reel

	#id_dimanche
	def get_id_dimanche(self):
		return self._id_dimanche

	def set_id_dimanche(self,id_dimanche):
		self._id_dimanche=id_dimanche

	#annee
	def get_annee(self):
		return self._annee

	def set_annee(self,annee):
		self._annee=annee

# Functionalities

	""" Permet de trouver la date correspondant a un id de dimance (1-52) d'une annee donner """
	def get_date_dimanche_of(sunday_number,year):
		# Trouver le premier jour de l'année
		first_day_of_year = date(year, 1, 1)
		
		# Calculer le jour de la semaine du premier jour de l'année (lundi=0, dimanche=6)
		day_of_week = first_day_of_year.weekday()
		
		# Si le premier jour de l'année n'est pas un dimanche (6), ajuster pour obtenir le premier dimanche
		if day_of_week != 6:
			first_sunday = first_day_of_year + timedelta(days=(6 - day_of_week))
		else:
			first_sunday = first_day_of_year
		
		# Ajouter le nombre de semaines nécessaires pour atteindre le dimanche souhaité 
		target_sunday = first_sunday + timedelta(weeks=(sunday_number - 1))
		
		return target_sunday
	
	""" String representative du contenue de la class """
	def to_string(self):
		return f"{self.get_date_reel()} is [{self.get_id_dimanche()}] of year {self.get_annee()}"

	""" Permet d'avoir la totaliter des dates de dimanche d'une annee specifique """
	def get_all_date_dimanche_of(year):
		array = list()
		# Pour chaque numero 1-52 en une annee definie on recupere la date correspondante
		for id in range(1,53):
			al = Alahady( date_reel=None,id_dimanche=id,annee=year)
			array.append( al )
		return array
	
	""" Permet d'obtenir le dimanche le plus recent """ 
	def get_closest_alahady(date_base = datetime.now().date() ):
		# Calculer le numero du jour baser ( son jour de la semaine ) 1-6
		weekly_num = date_base.weekday()
		# Calculer la difference entre le dimanche recent et la date donner
		target_sunday = date_base - timedelta(days=weekly_num+1)
  
		result = Alahady(date_reel=target_sunday)
		return result
	
	""" Permet d'avoir le numero de dimanche d'une date donnee """	
	def get_id_dimanche_by_date(ddate):
		if ddate.weekday() == 6:  # Vérifier si la ddate est un dimanche (0 pour lundi, 6 pour dimanche)
			# Trouver le premier dimanche de l'année
			first_day = date(ddate.year, 1, 1)
			while first_day.weekday() != 6:  # 6 représente le dimanche
				first_day += timedelta(days=1)

			# Calculer le nombre de semaines entre le premier dimanche et la ddate donnée
			num_weeks = (ddate - first_day).days // 7 + 1
			return num_weeks
		else:
			return -1  # Retourner None si la date n'est pas un dimanche