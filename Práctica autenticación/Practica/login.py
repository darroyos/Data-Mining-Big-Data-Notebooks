from pymongo.mongo_client import MongoClient


class Login():
    tiempo_presionado = 0
    tiempo_vuelo = 0
    usuario = None
    prediction = None


    def toTuple(self):
        return (self.tiempo_presionado, self.tiempo_vuelo, self.usuario)

    def predict(self, model):
        self.prediction = model.predict([self.toTuple()[:-1]])[0]

    def save(self):
        login = {
            "tiempo_presionado": self.tiempo_presionado,
            "tiempo_vuelo": self.tiempo_vuelo,
            "usuario": self.usuario
        }

        client = MongoClient('localhost', 27017)
        db = client['myDB']
        collection = db["login"]
        collection.insert_one(login)
