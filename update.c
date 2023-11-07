#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mysql.h>

int main(int argc, char *argv[] ) {

// Parámetros de conexión
MYSQL *conexion; // Conexion a servidor
char *servidor = "127.0.0.1"; // Nombre de Servidor
char *usuario = "gerardo"; //Usuario de la base de datos
char *contra = "54321";//Contraseña del usuario
char *basedatos = "ahorros"; // Nombre de la base de datos
int puerto = 13306; // Puerto del servicio

//Inicializando variable de conexion
conexion = mysql_init(NULL);
// Conexion a servidor de base de datos
if(!mysql_real_connect(conexion, servidor, usuario, contra, basedatos, puerto,  NULL, 0)){
      printf("Error: %s\n", mysql_error(conexion));
      exit(1);
 }
 
 // Establece la consultas a realizar
   char sqlForm[]= "UPDATE cuentas SET email='%s' WHERE id=%s";
   char sql[300];
   sprintf(sql, sqlForm, argv[2], argv[1]);

// Envia consulta SQL para la Cuenta
  if (mysql_query(conexion, sql)){
     printf("Error al ejecutar la consulta: %s\n", mysql_error(conexion));
     exit(1);
  } 

if(mysql_affected_rows(conexion)>0)
    printf("Registro Actualuzado correctamente\n");
  else
    printf("Registro NO existe\n");

  mysql_close(conexion);
}

