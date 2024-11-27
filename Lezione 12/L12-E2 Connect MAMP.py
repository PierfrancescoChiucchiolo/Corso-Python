'''
usa pythonsql
l'utente può inserire un alunno e i suoi voti in italiano e matematica
eliminare uno studente
modificare un voto o uno studente
stampare tutti gli studenti e le loro medie

'''



import mysql.connector as sql


## ESEGUITO SOLO LA PRIMA VOLTA


mydb = sql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    port = 3306
)


mycursor = mydb.cursor()

query = "create database if not exists registroscolastico"
mycursor.execute(query)




mydb = sql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    port = 3306,
    database = "registroscolastico"
)

## CONTIENE I VALORI DI RETURN DELLE QUERIES
mycursor = mydb.cursor()

## query = "create table alunni (nome varchar(50), italiano int, matematica int)"
## query = "insert into alunni values ('Gianni', 9, 6)"
## query = "delete from alunni where alunni.nome = 'Gianni'  "
## query = "update alunni set nome = 'gianni morandi', italiano = 10, matematica = 10 where nome = 'Gianni'  "
query = "select alunni.nome, sum( (alunni.italiano + alunni.matematica) / 2) from alunni group by alunni.nome"


mycursor.execute(query)
mydb.commit()