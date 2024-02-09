# Importar librerías
from pymongo import MongoClient
import json

# Conectarse a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['restaurants']
col = db['restaurants'] 

# Importar datos de restaurants.json
with open('restaurants.json') as f:
  file_data = json.load(f)

col.insert_many(file_data)

# Búsquedas

# Restaurantes grado B en Bronx
pipeline = [
  {"$match": {"borough": "Bronx", "grades.grade": "B"}},
  {"$project": {"name": 1, "grades": 1}}
]
for doc in col.aggregate(pipeline):
  print(doc)

# Restaurantes puntuación >30 
result = col.find({"grades.score": {"$gt": 30}}, {"name": 1})
for r in result:
  print(r)
  
# Restaurantes italianos en Brooklyn
result = col.find({"borough": "Brooklyn", "cuisine" : "Italian"}, {"name": 1})
for r in result:
  print(r)
  
# Ordenados por borough y zipcode  
result = col.find({}).sort([("borough", 1), ("address.zipcode", 1)])
for r in result:
  print(r)