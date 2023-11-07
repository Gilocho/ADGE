#include <stdio.h> 
#include <stdlib.h>
#include <mysql.h> 
#include <string.h>
#include <ctype.h>

// UDF que  retorne la cadena  como oración
_Bool Titulo_init(UDF_INIT *initid, UDF_ARGS *args, char *message) {
    if (args->arg_count != 1 || args->arg_type[0] != STRING_RESULT){
        strcpy (message, "Solo se permite un argumento, de cadena de caracteres");
        return 1;
    }
   int longitud =  args->lengths[0];
   initid->ptr=NULL;
   if(longitud>255){
      initid->ptr= (char *)malloc(sizeof(char) * longitud);
      if (initid->ptr==NULL){
        strcpy (message, "Problemas con malloc!!!");
        return 1;
      }
   }
   initid->max_length =longitud;
   return 0;
}

char *Titulo(UDF_INIT *initid, UDF_ARGS *args, char *result, unsigned long *res_length, char *is_null, char *error){
   int i, estado=0;
   char c;
  if (initid->ptr!=NULL)
      result =  initid->ptr;
   // copia el argumento cadena dentro del resultado
   memcpy(result, args->args[0], args->lengths[0]);
  *res_length = args->lengths[0];
   for (i=0; i<*res_length; i++){
     c =result[i]=tolower(result[i]);
      if (c == ' ')
         estado = 0; //fuera de palabra
      else if (estado == 0) {
         estado = 1;  //inicio de palabra
         if (isalpha(c))
                result[i] = toupper(c);
      }
    }
return result;
}

void Titulo_deinit(UDF_INIT *initid){
  if (initid->ptr!=NULL)
     free(initid->ptr);
}

// POTENCIA


// Función que calcula la potencia de un número
_Bool potencia_init(UDF_INIT *initid, UDF_ARGS *args, char *message)
{
    if (args->arg_count != 2)
    {
        strcpy(message, "La función potencia requiere exactamente dos argumentos.");
        return 1;
    }
    args->arg_type[0] = INT_RESULT;
    args->arg_type[1] = INT_RESULT;
    initid->maybe_null = 0;
    initid->ptr = NULL;
    return 0;
}

long long potencia(UDF_INIT *initid, UDF_ARGS *args, char *is_null, char *error)
{
    long long base = *((long long *)args->args[0]);
    long long exponente = *((long long *)args->args[1]);
    long long resultado = 1;

    for (long long i = 0; i < exponente; i++)
    {
        resultado *= base;
    }

    return resultado;
}

// Función que calcula la longitud de una cadena
_Bool longitud_init(UDF_INIT *initid, UDF_ARGS *args, char *message)
{
    if (args->arg_count != 1 || args->arg_type[0] != STRING_RESULT)
    {
        strcpy(message, "La función longitud requiere exactamente un argumento de tipo cadena.");
        return 1;
    }
    initid->maybe_null = 1;
    initid->max_length = 255;  // Establece la longitud máxima que esperas para la cadena
    initid->ptr = NULL;
    return 0;
}

long long longitud(UDF_INIT *initid, UDF_ARGS *args, char *is_null, char *error)
{
    if (args->args[0] == NULL)
    {
        *is_null = 1;
        return 0;
    }

    char *cadena = (char *)args->args[0];
    return((long long)strlen(cadena)+1);
}



