#include <stdio.h> 
#include <stdlib.h>
#include <mysql.h> 
#include <string.h>
#include <ctype.h>

MYSQL *conexion;
MYSQL_RES *resultados;
MYSQL_ROW registro;
char *servidor="localhost";
char *usuario="sammy";
char *contrasena ="password";
int puerto =3306;
char *basedatos="world";

int mysql_query(MYSQL * conexion, const char *consultaSQL);
int mysql_real_query(MYSQL *conexion, const char *consultaSQL, unsigned long tam);


int main(int argc, char *argv[])
{
conexion = mysql_init(NULL);
//conexion a servidor de base de datos
if(!mysql_real_connect(conexion, servidor, usuario, contrasena, basedatos,
puerto,NULL,0)){
    printf("Error %s\n",mysql_error(conexion));
    exit(1);
}
// Establece la consulta a realizar
char sqlForm[]= "SELECT * FROM cuentas  WHERE id = %s";

// Establece los parámetros de la consulta a realizar
sprintf(sql, sqlForm, argv[1]);

// Envia consulta SQL para la tabla Cuenta
  if (mysql_query(conexion, sql)){
     printf("Error: %s\n", mysql_error(conexion));
     exit(1);
  }

}