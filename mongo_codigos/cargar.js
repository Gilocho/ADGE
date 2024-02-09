var ultimos10= function(){
    return db.people.find({},{name:1}).sort({name:-1}).limit(10).pretty();
}
prompt=hostname()+"Luis>";
print("Datos cargados correctamente");