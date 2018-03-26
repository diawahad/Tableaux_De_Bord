/*------------------------------------------------------------
*        Script SQLSERVER 
------------------------------------------------------------*/


/*------------------------------------------------------------
-- Table: Articles
------------------------------------------------------------*/
CREATE TABLE Articles(
	Id_articles  INT IDENTITY (1,1) NOT NULL ,
	Date_Article VARCHAR (50)  ,
	Titre        VARCHAR (2500)  ,
	Introduction VARCHAR (2500)  ,
	CONSTRAINT prk_constraint_Articles PRIMARY KEY NONCLUSTERED (Id_articles)
);


/*------------------------------------------------------------
-- Table: Auteurs
------------------------------------------------------------*/
CREATE TABLE Auteurs(
	Id_auteurs INT IDENTITY (1,1) NOT NULL ,
	Nom        VARCHAR (250)  ,
	Prenom     VARCHAR (250)  ,
	CONSTRAINT prk_constraint_Auteurs PRIMARY KEY NONCLUSTERED (Id_auteurs)
);


/*------------------------------------------------------------
-- Table: Mots_cles
------------------------------------------------------------*/
CREATE TABLE Mots_cles(
	Id_mots_cles INT IDENTITY (1,1) NOT NULL ,
	Mots1        VARCHAR (2500)  ,
	Mots2        VARCHAR (2500)  ,
	CONSTRAINT prk_constraint_Mots_cles PRIMARY KEY NONCLUSTERED (Id_mots_cles)
);


/*------------------------------------------------------------
-- Table: Associer
------------------------------------------------------------*/
CREATE TABLE Associer(
	freq1        INT   ,
	freq2        INT   ,
	Id_articles  INT  NOT NULL ,
	Id_mots_cles INT  NOT NULL ,
	CONSTRAINT prk_constraint_Associer PRIMARY KEY NONCLUSTERED (Id_articles,Id_mots_cles)
);


/*------------------------------------------------------------
-- Table: Ecrire
------------------------------------------------------------*/
CREATE TABLE Ecrire(
	Id_articles INT  NOT NULL ,
	Id_auteurs  INT  NOT NULL ,
	CONSTRAINT prk_constraint_Ecrire PRIMARY KEY NONCLUSTERED (Id_articles,Id_auteurs)
);



ALTER TABLE Associer ADD CONSTRAINT FK_Associer_Id_articles FOREIGN KEY (Id_articles) REFERENCES Articles(Id_articles);
ALTER TABLE Associer ADD CONSTRAINT FK_Associer_Id_mots_cles FOREIGN KEY (Id_mots_cles) REFERENCES Mots_cles(Id_mots_cles);
ALTER TABLE Ecrire ADD CONSTRAINT FK_Ecrire_Id_articles FOREIGN KEY (Id_articles) REFERENCES Articles(Id_articles);
ALTER TABLE Ecrire ADD CONSTRAINT FK_Ecrire_Id_auteurs FOREIGN KEY (Id_auteurs) REFERENCES Auteurs(Id_auteurs);
