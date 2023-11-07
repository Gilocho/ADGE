import mysql.connector

# Conectarse a MySQL (asegúrate de tener el servidor MySQL en funcionamiento)
conexion = mysql.connector.connect(
    host="localhost",
    user="sammy",
    password="password"
)

# Crear una instancia del cursor
cursor = conexion.cursor()

# Crear la base de datos
cursor.execute("CREATE DATABASE IF NOT EXISTS tarea2")
print("Base de datos creada")

# Seleccionar la base de datos recién creada
cursor.execute("USE tarea2")

# Crear la tabla 'cuentas'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cuentas (
        id INT(11) AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(40),
        email VARCHAR(30),
        fecha DATETIME,
        foto BLOB
    )
""")
print("Tabla 'cuentas' creada")

# Crear la tabla 'movimientos'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS movimientos (
        idmov INT(11) AUTO_INCREMENT PRIMARY KEY,
        idicuenta INT(11),
        fechamov DATETIME,
        tipo CHAR(1),
        cantidad FLOAT,
        FOREIGN KEY (idicuenta) REFERENCES cuentas(id)
    )
""")
print("Tabla 'movimientos' creada")

# Cerrar la conexión a MySQL
cursor.close()
conexion.close()