// Promedio de edad por género
var mapFunction = function() {
    if (this.isActive && this.antiguedad < 10) {
      emit(this.gender, {edad: this.age, count: 1}); 
    }
  }
  
  var reduceFunction = function(key, values) {
    let resultado = {sumaEdades: 0, count: 0};
  
    values.forEach(value => {
      resultado.sumaEdades += value.edad;
      resultado.count += value.count;
    });
  
    return {
      promedio: resultado.sumaEdades / resultado.count
    };
  }
  
  db.coleccion.mapReduce(mapFunction, reduceFunction, {out: "resultado"});
  
  // Balance global por género 
  var mapFunction = function() {
    emit(this.gender, this.balance);
  }  
  
  var reduceFunction = function(key, values) {
    return Array.sum(values); 
  }
  
  // Total balance por año
  var mapFunction = function() {
    emit(this.year, this.balance);  
  }
  
  var reduceFunction = function(key, values) {
    return Array.sum(values);
  }
  
  // Total balance activos por año 
  var mapFunction = function() {
    if (this.isActive) {
      emit(this.year, this.balance);
    }
  }
  
  var reduceFunction = function(key, values) {
    return Array.sum(values);
  }