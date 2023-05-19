from pymongo import MongoClient

def obtenerConexion():
    client = MongoClient('mongodb+srv://gaelcuevasm:gas18265@cursoholamundo.oxfqwcs.mongodb.net/?retryWrites=true&w=majority')

    dataBase=client['QrDatabase']

    return dataBase


