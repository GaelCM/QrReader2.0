from pymongo import MongoClient

client = MongoClient('mongodb+srv://gaelcuevasm:gas18265@cursoholamundo.oxfqwcs.mongodb.net/?retryWrites=true&w=majority')
db = client['QrDataBase']
collection = db['Alumnos']

nuevoDocumento={
    'numControl':'L20920104',
    'nombre':'Fernanda',
    'carrera':'ing.informática',
    'semestre': 6
}

resultado=collection.insert_one(nuevoDocumento)

idInsertado=resultado.inserted_id

print(idInsertado)