// Conectarse a la BD sinaloadb
use sinaloadb

// Insertar municipios
db.municipios.insertMany([
  {nombre: "Ahome", habitantes: 450000, área: 3000},
  {nombre: "Guasave", habitantes: 350000, área: 5500}, 
  {nombre: "Culiacán", habitantes: 900000, área: 4000},
  {nombre: "Mazatlán", habitantes: 500000, área: 3200}
])

// Insertar presidentes municipales 
db.presidentes.insertMany([
  {municipio: "Ahome", presidente: "Billy Chapman"},
  {municipio: "Guasave", presidente: "Martín Ahumada"},
  {municipio: "Culiacán", presidente: "Jesús Estrada"},
  {municipio: "Mazatlán", presidente: "Luis Benítez"}  
])