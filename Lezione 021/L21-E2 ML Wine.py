'''

1. Carica il dataset Wine
Carica il dataset Wine dal modulo datasets di scikit-learn.

2. Standardizza le caratteristiche
Standardizza le caratteristiche utilizzando StandardScaler per portare tutte
le feature su una scala comune.

3. Suddividi i dati in training e test set
Suddividi i dati in due set: il 70% per il training e il 30% per il test.

4. Applica un algoritmo di classificazione
Applica l'algoritmo DecisionTreeClassifier per la classificazione.

5. Valuta la performance del modello
Valuta la performance del modello utilizzando il classification_report, con
metriche come precisione, recall e F1-score.

6. Visualizza la matrice di confusione
Genera e visualizza la matrice di confusione per valutare la qualità della
classificazione.

'''

from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier

from sklearn.model_selection import cross_val_score

from sklearn.metrics import confusion_matrix

from sklearn.metrics import classification_report




## from sklearn.datasets import load_wine
data = load_wine()
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


from sklearn.model_selection import cross_val_score

scores = cross_val_score(data, X, y, cv=5)
print(f"Scores: {scores}")


print(classification_report(y_test, y_train))

## rubato da https://scikit-learn.org/stable/modules/generated/sklearn.metrics.confusion_matrix.html
confusion_matrix(y_test, y_train)

