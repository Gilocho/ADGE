#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mysql.h>

int main(int argc, char *argv[] ) {
// Parámetros de conexión
 MYSQL *conexion; // Conexion a servidor
 char *servidor = "127.0.0.1"; // Nombre de Servidor
 char *usuario = "admin"; //Usuario de la base de datos   
 char *contra= "12AB34cd"; //Contraseña del usuario  
 char *basedatos = "ahorros";  // Nombre de la base de datos 
 int puerto = 13306; // Puerto del servicio
 conexion = mysql_init(NULL); //Inicializando variable de conexion
 
// Conexion a servidor de base de datos
 if(!mysql_real_connect(conexion, servidor, usuario, contra, basedatos, puerto,  NULL, 0)){
      printf("Error: %s\n", mysql_error(conexion));
      exit(1);
  }
// Establece la consultas a realizar
char sqlForm[]= "INSERT INTO cuentas (nombre, email, fecha) VALUES ('%s', '%s', '%s')";
char sql[300];
sprintf(sql, sqlForm, argv[1], argv[2], argv[3]);

// Envia consulta SQL para la Cuenta
if (mysql_query(conexion, sql)){
    printf("Error al ejecutar la consulta: %s\n", mysql_error(conexion));
    exit(1);
 }

  int num = mysql_affected_rows(conexion);

  printf("Se agrego %d registro correctamente \n", num );

  mysql_close(conexion);
}
