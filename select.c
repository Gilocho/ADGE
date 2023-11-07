#include <stdio.h> 
#include <stdlib.h>
#include <mysql.h> 
int main() {
// Parámetros de conexión
MYSQL *conexion;  // Conexión a servidor  
MYSQL_RES *resultados; // Recuperación de resultados   
MYSQL_ROW registro;  // Recuperación de registros  
char *servidor = "127.0.0.1"; // Nombre o IP del Servidor 
char *usuario = "admin"; //Usuario de la base de datos   
char *contra= "12AB34cd"; //Contraseña del usuario  
char *basedatos = "ahorros";  // Nombre de la base de datos 
int puerto = 13306; // Puerto del servicio
conexion = mysql_init(NULL); //Inicializando variable de conexión   

// Conexión a servidor de base de datos   
if(!mysql_real_connect(conexion, servidor, usuario, contra, basedatos, puerto, NULL, 0)){     
    printf("%s\n", mysql_error(conexion));     // Mensaje del posible error 
    exit(1);  
}   
// Ejecuta consulta SQL   
if (mysql_query(conexion, "SELECT * FROM cuentas")) {     
 printf("%s\n", mysql_error(conexion));     
 exit(1); 
 }  
// Recupera dirección de los resultados  
resultados = mysql_store_result(conexion);  
int num = mysql_num_rows(resultados); // numero de registros recuperados

printf("Lista de %d clientes\n", num);
// Muestra registros de tabla  
printf("Lista de clientes\n");
printf("%8s %-25s %-30s\n", "Cuenta", "Nombre", "Correo");  
while ((registro = mysql_fetch_row(resultados)) != NULL)     
    printf("%8s %-25s %-30s\n", registro[0], registro[1],registro[2]);   

mysql_free_result(resultados);  // Liberar recursos de resultados
mysql_close(conexion); // Cierra conexión  
return 0;
}
