CREATE TABLE Mpino(
   idMpino INT IDENTITY(1,1),
   login VARCHAR(50)  NOT NULL,
   nomMpino VARCHAR(50)  NOT NULL,
   password VARCHAR(50)  NOT NULL,
   PRIMARY KEY(idMpino)
);

CREATE TABLE Pret(
   idPret INT IDENTITY(1,1),
   datePret DATE,
   montant DECIMAL  NOT NULL,
   idMpino INT,
   PRIMARY KEY(idPret),
   FOREIGN KEY(idMpino) REFERENCES Mpino(idMpino)
);
insert into Pret (datePret , montant , idMpino)
values ('2024-01-01' , 0 , 1)

CREATE TABLE Rakitra(
   idRakitra INT IDENTITY(1,1),
   montant DECIMAL NOT NULL,
   dateDepot DATE NOT NULL,
   PRIMARY KEY(idRakitra),
   UNIQUE(dateDepot)
);

-- Insertion de données pour l'année 2022
DECLARE @StartDate2022 DATE = '2022-01-01';
DECLARE @EndDate2022 DATE = '2022-12-31';

WHILE @StartDate2022 <= @EndDate2022
BEGIN
    -- Insertion de données pour chaque dimanche
    IF DATEPART(weekday, @StartDate2022) = 1
    BEGIN
        INSERT INTO Rakitra ( montant, dateDepot)
        VALUES (6800, @StartDate2022);
    END

    -- Passage au jour suivant
    SET @StartDate2022 = DATEADD(day, 1, @StartDate2022);
END;

-- Insertion de données pour l'année 2023
DECLARE @StartDate2023 DATE = '2023-01-01';
DECLARE @EndDate2023 DATE = '2023-12-31';

WHILE @StartDate2023 <= @EndDate2023
BEGIN
    -- Insertion de données pour chaque dimanche
    IF DATEPART(weekday, @StartDate2023) = 1
    BEGIN
        INSERT INTO Rakitra ( montant, dateDepot)
        VALUES (10000, @StartDate2023);
    END

    -- Passage au jour suivant
    SET @StartDate2023 = DATEADD(day, 1, @StartDate2023);
END;

-- Insertion de données pour les neuf premiers dimanches de 2024
DECLARE @StartDate2024 DATE = '2024-01-01';
DECLARE @EndDate2024 DATE = '2024-12-31';
DECLARE @SundayCount INT = 0;

WHILE @StartDate2024 <= @EndDate2024 AND @SundayCount < 9
BEGIN
    -- Insertion de données pour chaque dimanche
    IF DATEPART(weekday, @StartDate2024) = 1
    BEGIN
        INSERT INTO Rakitra ( montant, dateDepot)
        VALUES (12500, @StartDate2024);
        
        SET @SundayCount = @SundayCount + 1;
    END

    -- Passage au jour suivant
    SET @StartDate2024 = DATEADD(day, 1, @StartDate2024);
END;


-- View
create  view v_sum_montants as 
select (select sum(montant) from Rakitra) as sum_rk , (select sum(montant) from Pret) as sum_pr

create view v_caisse as 
select (select (sum_rk - sum_pr) from v_sum_montants) as montant_actuelle , (select MAX(datePret) from Pret) as date_dispo