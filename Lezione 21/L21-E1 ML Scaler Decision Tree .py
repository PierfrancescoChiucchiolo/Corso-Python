'''

Carica il dataset Iris.
Standardizza le caratteristiche
utilizzando StandardScaler.
Suddividi i dati in training e test set
(70% training, 30% test).
Applica l'algoritmo
DecisionTreeClassifier.
Valuta la performance del modello
utilizzando il classification_report
(precisione, recall, F1-score).
Visualizza la matrice di confusione.

'''


from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier


## from sklearn.datasets import load_iris
data = load_iris()
X = data.data  # caratteristiche
y = data.target  # target

## inizializzo lo scaler con costruttore vuoto, normalizzo i dati
## codice strappato da https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

## from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)

## strappato da https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
clf = DecisionTreeClassifier(random_state = 42)
clf.fit(X_train, y_train)

## prendo la predizione similarmente a come si chiede a knn, li usavo knn.predict(X_test), qui è uguale ma cambia il modello
y_pred = clf.predict(X_test)

## uguale a prima, strappato dal codice dell'esercizio precedente
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuratezza del modello: {accuracy:.2f}")