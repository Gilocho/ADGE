
// Consulta 01: Obtener los nombres de las personas que tengan una edad específica.
var consulta01 = function(edad) {
    return db.coleccion.find({edad: edad}, {nombre: 1}).pretty(); 
  }
// Consulta 02: Obtener los nombres de las personas que tengan una edad específica y sean de un género específico.
consulta02 = function(antiguedad, sexo, mes){
    return db.coleccion.find({antiguedad: {$lt: antiguedad}, sexo: sexo, fecha: {$regex: mes}}).pretty();
  }
  // Consulta 03: Obtener los nombres de las personas que tengan una antigüedad en la empresa entre un rango de fechas.
  db.system.js.save({
    _id: "consulta03",
    value: function(inicio, fin){
      return db.coleccion.find({antiguedad: {$gte: inicio, $lte: fin}}).pretty();
    }
  })

  //consulta 04: Obtener los nombres de las personas que tengan una antigüedad en la empresa mayor a un número de años y que hayan ingresado antes de una hora específica.
  var consulta04 = function(anios, hora){
    return db.coleccion.find({activo: true, antiguedad: {$gt: anios}, fecha: {$lt: hora}}).pretty();
  }