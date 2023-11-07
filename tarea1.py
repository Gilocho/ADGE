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
cursor.execute("CREATE DATABASE IF NOT EXISTS tarea1")
print("Base de datos creada")

# Seleccionar la base de datos recién creada
cursor.execute("USE tarea1")

# Crear la tabla 'cliente'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS cliente (
        RFC_Cliente VARCHAR(100) PRIMARY KEY,
        Nombre VARCHAR(40),
        Apellido1 VARCHAR(40),
        Apellido2 VARCHAR(40),
        Nombre_Empresa VARCHAR(100),
        Direccion VARCHAR(200),
        Ciudad VARCHAR(50),
        Estado VARCHAR(50),
        CP CHAR(5)
    )
""")
print("Tabla 'cliente' creada")

# Crear la tabla 'factura'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS factura (
        Num_Factura INT(11) PRIMARY KEY,
        idicuenta INT(11),
        Fecha_Factura DATE,
        RFC_Cliente VARCHAR(100),
        FOREIGN KEY (RFC_Cliente) REFERENCES cliente(RFC_Cliente)
    )
""")
print("Tabla 'factura' creada")

# Crear la tabla 'proveedor'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS proveedor (
       RFC_Proveedor VARCHAR(100) PRIMARY KEY,
        Nombre VARCHAR(40),
        Apellido1 VARCHAR(40),
        Apellido2 VARCHAR(40),
        Nombre_Empresa VARCHAR(100),
        Direccion VARCHAR(200),
        Ciudad VARCHAR(50),
        Estado VARCHAR(50),
        CP CHAR(5)         
    )
""")
print("Tabla 'proveedor' creada")
# Crear la tabla 'articulo'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS articulo (
        Cod_Articulo INT(11) PRIMARY KEY,
        RFC_Proveedor VARCHAR(100),
        Nombre_Articulo VARCHAR(200),
        Caracteristicas VARCHAR(200),
        Precio FLOAT,
        FOREIGN KEY (RFC_Proveedor) REFERENCES proveedor(RFC_Proveedor)
        
    )
""")
print("Tabla 'articulo' creada")

# Crear la tabla 'detallefactura'
cursor.execute("""
    CREATE TABLE IF NOT EXISTS detallefactura (
        Num_DetalleFactura INT(11) AUTO_INCREMENT PRIMARY KEY,
        Num_Factura INT(11),
        Cod_Articulo INT(11),
        Cantidad INT(11),
        FOREIGN KEY (Num_Factura) REFERENCES factura(Num_Factura),
        FOREIGN KEY (Cod_Articulo) REFERENCES articulo(Cod_Articulo)
    )
""")
print("Tabla 'detallefactura' creada")

# Cerrar la conexión a MySQL
cursor.close()
conexion.close()