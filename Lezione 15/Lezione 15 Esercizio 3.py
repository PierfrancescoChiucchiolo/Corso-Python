'''

calcolare la media dei voti per ogni materia

calcolare la media dei voti di ogni studente

calcolare la media di ogni studente in ogni materia

aggiungi riga in più e studenti

'''

import pandas as pd
import numpy as np
import random


data = {
'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie'],
'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science', 'English', 'English', 'English'],
'Score': [85, 90, 95, 80, 70, 75, 88, 92, 85]
}
df = pd.DataFrame(data)


media_materia = df.groupby("Subject")["Score"].mean()
print(media_materia)


media_studente = df.groupby("Student")["Score"].mean()
print(media_studente)

media_materia_studente = df.groupby(["Subject","Student"])["Score"].mean()
print(media_materia_studente)





data = {
'Student': ['Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Alice', 'Bob', 'Charlie', 'Delson', 'Delson', 'Delson'],
'Subject': ['Math', 'Math', 'Math', 'Science', 'Science', 'Science', 'English', 'English', 'English','Math', 'Science', 'English'],
'Score': [85, 90, 95, 80, 70, 75, 88, 92, 85, 90, 100, 95]
}
df = pd.DataFrame(data)


media_materia = df.groupby("Subject")["Score"].mean()
print(media_materia)


media_studente = df.groupby("Student")["Score"].mean()
print(media_studente)

media_materia_studente = df.groupby(["Subject","Student"])["Score"].mean()
print(media_materia_studente)