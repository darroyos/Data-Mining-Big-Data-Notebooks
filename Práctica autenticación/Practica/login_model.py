from login import Login
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score, GridSearchCV
from pymongo.mongo_client import MongoClient
from sklearn.externals import joblib
import time


# Conexión con la base de datos
client = MongoClient('localhost', 27017)
db = client['myDB']
collection = db["login"]

# Rutina de entrenamiento
def train():
    records = []
    for v  in collection.find({}):
        login = Login()
        login.tiempo_presionado = v["tiempo_presionado"]
        login.tiempo_vuelo = v["tiempo_vuelo"]
        login.usuario = v["usuario"]
        records.append(login.toTuple())

    features = ["tiempo_presionado", "tiempo_vuelo"]
    target = "usuario"

    labels =  features + [target]
    df = pd.DataFrame.from_records(records, columns = labels)

    # filtrado de outliers
    df = df[df['tiempo_presionado'] < 200]
    df = df[df['tiempo_vuelo'] < 350]

    algo = GradientBoostingClassifier(random_state=7)

    param_grid = {'n_estimators': [100, 105, 110, 115, 120], 'learning_rate': [0.1, 0.2, 0.3, 0.5]}

    X = df[features]
    y = df[target]

    clf = GridSearchCV(algo, param_grid)
    clf.fit(X, y)

    scores = cross_val_score(clf, X, y, cv=5)
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    # Exportamos el modelo
    joblib.dump(clf, 'gradient_boosting.pkl',  protocol=2)
    print("DUMP")


while True:
  train()
  time.sleep(3)
