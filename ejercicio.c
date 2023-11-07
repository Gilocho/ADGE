#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <mysql.h>
014133567240203076 
int id=0;

int main(int argc, char *argv[] ) {
    MYSQL *conexion;  // Conexión a servidor  
    MYSQL_RES *resultados; // Recuperación de resultados   
    MYSQL_ROW registro;  // Recuperación de registros  
    char *servidor = "127.0.0.1"; // Nombre o IP del Servidor 
    char *usuario = "admin"; //Usuario de la base de datos   
    char *contra= "12AB34cd"; //Contraseña del usuario  
    char *basedatos = "ahorros";  // Nombre de la base de datos 
    int puerto = 13306; // Puerto del servicio
    conexion = mysql_init(NULL); //Inicializando variable de conexión   
    if(!mysql_real_connect(conexion, servidor, usuario, contra, basedatos, puerto,  NULL, 0)){
          printf("Error: %s\n", mysql_error(conexion));
         exit(1);
    }
    printf("id a analizar:");
    scanf("%d", id);
    char sqlForm[]= "DELETE FROM cuentas WHERE id=%s";
   char sql[300];
   sprintf(sql, sqlForm, argv[1]);


}