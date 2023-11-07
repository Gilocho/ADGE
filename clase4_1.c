//ejemplo agregacion.
#include <stdio.h> 
#include <stdlib.h>
#include <mysql.h> 
#include <string.h>
#include <ctype.h>
typedef struct {
  double   total;
}info;

_Bool sumatoria_init(UDF_INIT *initid, UDF_ARGS *args, char *message) {
    if (args->arg_count != 1 || args->arg_type[0] != REAL_RESULT){
        strcpy (message, "Solo se permite un argumento, y debe de se de tipo real");
        return 1;
    }
   info *datos;
   datos = (info *) malloc (sizeof(info));
   if (datos==NULL){
        strcpy (message, "Error al Asignar memoria con malloc");
        return 1;
   }
   initid->ptr = (char *)datos;
   return 0;
}
void sumatoria_deinit(UDF_INIT *initid){
    free(initid->ptr);
}

void sumatoria_clear(UDF_INIT *initid, char *is_null,     char *error){
   info *datos = (info *)initid->ptr;
   datos->total=0;
}

void sumatoria_add(UDF_INIT *initid, UDF_ARGS *args, char *is_null, char *error){
    info *datos = (info *)initid->ptr;
    datos->total=datos->total+(*((double*)args->args[0]));
}

double sumatoria(UDF_INIT *initid, UDF_ARGS *args, char *is_null, char *error){
  info *datos = (info *)initid->ptr;
  double resultado =  datos->total;
return resultado;
}