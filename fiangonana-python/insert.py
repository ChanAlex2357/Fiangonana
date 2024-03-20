from models.alahady import Alahady
def saveIntoFile(fileOutput , content):
    fileOutput = f"{fileOutput}"
    fileOutput = open(fileOutput,"a+")
    fileOutput.write(content)
    fileOutput.close()

def enregistrer_script( id_date : int , list_values : list):
    fileoutput = "script.sql"
    annee = [2022 , 2023 , 2024]
    script = f"-- Id semaine [{id_date}]\n"
    for i in range(3):
        if( list_values[i] == 0):
            pass
        else :
            date = Alahady.get_date_dimanche_of(id_date,annee[i])
            script += f"INSERT INTO Rakitra(montant,dateDepot) values({list_values[i]},'{date}');\n"
    saveIntoFile(fileoutput,script)
while True :
    print("-----------------------")
    id_date = input("Numero date : ")
    montant = []
    montant.append( int(input("2022 : ")) )
    montant.append( int(input("2023 : ")) )
    montant.append( 0 )
    enregistrer_script(int(id_date),montant)