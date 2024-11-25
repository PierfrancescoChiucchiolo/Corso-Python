
'''


Carica il dataset Iris.
Suddividi i dati in training e test.
Applica l'algoritmo K-Nearest Neighbors
con n_neighbors=5.
Valuta la performance del modello
usando l'accuratezza.

Dataset Iris:
Contiene 150 campioni di fiori Iris.
Ogni campione ha 4 caratteristiche:
Lunghezza del sepalo (in cm).
Larghezza del sepalo (in cm).
Lunghezza del petalo (in cm).
Larghezza del petalo (in cm).
Tre classi (specie di Iris):
0: Iris Setosa.
1: Iris Versicolor.
2: Iris Virginica.

'''


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


## carico iris

## from sklearn.datasets import load_iris
data = load_iris()
X = data.data  # caratteristiche
y = data.target  # target


## divido training e test

## from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


## applico KNN / K-Nearest Neighbors (CON 5 NEIGHBORS)

## from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors = 5)
knn.fit(X, y)
predictions = knn.predict(X)


# Addestrare il modello sui dati di training

knn.fit(X_train, y_train)


# Fare predizioni sui dati di test

y_pred = knn.predict(X_test)


## valuto la performance

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza del modello: {accuracy:.2f}")
