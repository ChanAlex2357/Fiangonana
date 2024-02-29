CREATE TABLE Mpino(
   idMpino INT,
   login VARCHAR(50)  NOT NULL,
   nomMpino VARCHAR(50)  NOT NULL,
   password VARCHAR(50)  NOT NULL,
   PRIMARY KEY(idMpino)
);

CREATE TABLE Rakitra(
   idRakitra INT,
   montant INT NOT NULL,
   dateDepot DATE NOT NULL,
   PRIMARY KEY(idRakitra),
   UNIQUE(dateDepot)
);

CREATE TABLE Pret(
   idPret INT,
   datePret DATE,
   montant VARCHAR(50)  NOT NULL,
   idMpino INT,
   PRIMARY KEY(idPret),
   FOREIGN KEY(idMpino) REFERENCES Mpino(idMpino)
);
