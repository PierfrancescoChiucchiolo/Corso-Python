''' test 

select
from
where
group by
having (ulteriore filtro su group by)
group by

having (true/false esistenza)
any (true se almeno uno ha true)


(case
    when ...
    when ...
    else
end)

viste = tabelle virtuali basate su queries
create or replace view xxx as query


pip install mysql-connector-python



'''


import mysql.connector as sql

mydb = sql.connect(
    host = "localhost",
    user = "root",
    password = "root",
    port = 3306,
    database = "pythonmysql"
)

print(mydb)

## ci serve un cursore per navigare il database
mycursor = mydb.cursor()


'''
già eseguita e da errore se la rieseguo
query = "create table utenti (nome varchar(50), indirizzo varchar(50))"
mycursor.execute(query)
'''


## usiamo %s per resistere ad sql injection
query = "insert into utenti (nome, indirizzo) values(%s, %s)"
valori = ("Gianni", "Via Morandi")
mycursor.execute(query, valori)

mydb.commit()