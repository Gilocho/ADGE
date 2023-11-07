#include <stdio.h>
#include <stdlib.h>
#include <mysql.h>

int main() {
// Parámetros de conexión
MYSQL *conexion;  // Conexión a servidor
MYSQL_RES *resultados; // Recuperación de resultados
MYSQL_ROW registro;  // Recuperación de registros
char *servidor="localhost";
char *usuario="sammy";
char *contra ="password";
int puerto =3306;
char *basedatos="ahorros";
conexion = mysql_init(NULL); //Inicializando variable de conexió
int i;

// Conexión a servidor de base de datos
if(!mysql_real_connect(conexion, servidor, usuario, contra, basedatos, puerto, NULL, 0)){
    printf("%s\n", mysql_error(conexion));     // Mensaje del posible error
    exit(1);
}


// información de conexión
printf("Versión del Servidor: %s\n", conexion->server_version);
printf("Nombre de Base de Datos: %s\n", conexion->db);
printf("Nombre del Servidor: %s\n", conexion->host);
printf("Nombre del Usuario: %s\n", conexion->user);
printf("Nombre del Contraseña: %s\n", conexion->passwd);

// Ejecuta consulta SQL
if (mysql_query(conexion, "SELECT * FROM cuentas")) {
 printf("%s\n", mysql_error(conexion));
exit(1);
 }
// Recupera dirección de los resultados
resultados = mysql_store_result(conexion);
 // Recupera definición de campos de la tabla
MYSQL_FIELD  *campos;
int numCampos = resultados->field_count;
printf("         %-10s %10s %10s \n", "Nombre", "Tipo", "Tamaño");
campos=resultados->fields; // Recupera dirección inicial  de los campos
for(i=0; i< numCampos; i++){
  printf("Campo %d: %-10s %10d %10lu \n", i+1, campos->name, campos->type, campos->length);
  campos++;
}

//Muestra registros de tabla
printf("%12s %-29s %-34s\n", "Cuenta", "Nombre", "Correo");
while ((registro = mysql_fetch_row(resultados)) != NULL){
  unsigned long *longitud = resultados->lengths;
  printf("%8s(%2lu) %-25s(%2lu) %-30s(%2lu)\n", registro[0], longitud[0],registro[1], longitud[1], registro[2], longitud[2], registro[3], longitud[3]);
}
printf("Lista de %d clientes\n",(int) resultados->row_count);
mysql_free_result(resultados);  // Liberar recursos de resultados
mysql_close(conexion); // Cierra conexión
return 0;
}
