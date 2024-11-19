'''

la media dello stipendio e dell'esperienza per ogni dipartimento

trovare i dipendenti con uno stipendio sopra la media

aggiungere una nuova colonna che rappresenta il rank (consiglio cercate la funzione rank di pandas) di ogni dipendente all'interno del suo dipartimento

Mostrare il fataframe raggruppato per dipartimento e ogni dipendente in ordine dal rank più alto al più basso

rank in base allo stipendio


'''




import pandas as pd
import numpy as np

# Larger employee dataset
data = {
'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva', 'Frank', 'Grace', 'Hannah', 'Ian', 'Jack', 'Kara', 'Liam'],
'Department': ['HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT', 'HR', 'Finance', 'IT'],
'Salary': [50000, 60000, 70000, 52000, 58000, 72000, 55000, 62000, 75000, 51000, 63000, 76000],
'Experience': [2, 5, 8, 3, 4, 10, 4, 6, 12, 1, 7, 15]
}
df = pd.DataFrame(data)

media_stipendio = df["Salary"].mean()
print(media_stipendio)
dipendenti_media_stipendio = df.loc[df["Salary"] >= media_stipendio, ["Name", "Salary"]]
print(dipendenti_media_stipendio)

df["Rank Salary Department"] = df.groupby("Department")["Salary"].rank()
dipendenti_department_rank = df.sort_values(by = "Department", ascending = False)
print(dipendenti_department_rank)

df["Rank Salary Absolute"] = df["Salary"].rank()
dipendenti_salary_rank = df.sort_values(by = "Rank Salary Absolute", ascending = False)
print(dipendenti_department_rank)

