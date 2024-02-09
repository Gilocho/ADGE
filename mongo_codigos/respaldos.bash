# Respaldar documentos activos y sexo femenino
mongodump --db test --collection people --query '{"isActive": true, "gender": "female"}' --out respaldo/activos_femenino

# Respaldar edades entre 40 y 60 años (comprimido)
mongodump --db test --collection people --query '{"age": {$gte: 40, $lte: 60}}' --gzip --out respaldo/edades40_60

# Restaurar en otra BD 
mongorestore --db nuevadb --collection gente --drop --archive=respaldo/activos_femenino/test/people.bson 

mongorestore --db nuevadb --collection gente --drop --archive=respaldo/edades40_60/test/people.bson.gz