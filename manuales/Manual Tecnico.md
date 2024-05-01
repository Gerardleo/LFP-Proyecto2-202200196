#Proyecto No.2 - Lenguajes Formales y de Programacion

# Manual de Tecnico - Lectura de Archivos bizdata

**Nombre:** Gerardo Leonel Ortiz Tobar
**Carnet:** 202200196


# Analizador Lexico (lexico.py)
Se presenta el analizador lexico de la lectura de archivos bizdata


La funcion lexico se encarga de analizar el archivo que se esta utilizando y mostrar los resultos que se encuentren

# Declaraciones Iniciales
En esta sección, se crea una lista_tokens para almacenar los tokens generados durante el análisis léxico, y una lista_errores para almacenar los errores léxicos. También se definen algunas variables y expresiones regulares utilizadas en el análisis.

![funcionLexico1](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/LEXICO%201.png)
![funcionLexico2](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/LEXICO%202.png)
![funcionLexico3](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/LEXICO%203.png)

# Funciones de Análisis

El código incluye funciones para el análisis léxico de la entrada. armar_lexema se encarga de construir lexemas a partir de la entrada, y agregar_token y agregar_error se utilizan para agregar tokens y errores a las listas correspondientes.



# Funciones de Gestión de Errores
Estas funciones se encargan de obtener y limpiar los errores léxicos generados durante el análisis. retornarErroresLexico devuelve los errores léxicos en objeto, y limpiarErroresLexicos los borra.

# Funciones Adicionales 
![limpiar](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/limpiar%20tecnico.png)
La función limpiarCampos se utiliza para reiniciar algunas variables y estructuras de datos específicas utilizadas en el análisis.


# Analizador Sintactico (sintactico.py)
Se presenta el analizador sintactico de la lectura de archivos bizdata

![sintactico1](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/Sintatico%201.png)
![sintactico2](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/Sintatico%202.png)
![sintactico3](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/Sintatico%203.png)

La funcion sintactico se encarga de analizar el archivo que se esta utilizando y mostrar los resultos que se encuentren

![funcion](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/Funcion.png)

# Métodos de Análisis de Instrucciones
 El código proporciona métodos para analizar instrucciones específicas, como la de CrearDB, EliminarDB, CrerColeccionDB, EliminarColeccionDB, InsertarUnico, ActualizarUnico, EliminarUnico, BuscarUnico y BuscarTodo.


# Gramatica
La gramatica utilizada para el analizador sintactico es la siguiente:

```
INICIO ->  LISTA_INSTRUCCIONES 

    LISTA_INSTRUCCIONES -> INSTRUCCION LISTA_INSTRUCCIONES
                         | Epsilon

    INSTRUCCION ->  CrearDB
                 | EliminarDB
                 | CrerColeccionDB
                 | EliminarColeccionDB
                 | InsertarUnico
                 | ActualizarUnico
                 | EliminarUnico
                 | BuscarUnico
                 | BuscarTodo
                 

    CrearDB -> PALABRARESERVADA NOMBRE IGUAL STRING PALABRARESERVADA CORCHETEIZQUIERDO CORCHETEDERECHO PUNTOYCOMA 

    EliminarDB -> PALABRARESERVADA NOMBRE IGUAL STRING PALABRARESERVADA CORCHETEIZQUIERDO CORCHETEDERECHO PUNTOYCOMA

    CrerColeccionDB -> PALABRARESERVADA NOMBRE PUNTO NOMBRE IGUAL PALABRARESERVADA CORCHETEIZQUIERDO NOMBRECOLEECCION CORCHETEDERECHO PUNTOYCOMA

    EliminarColeccionDB -> PALABRARESERVADA NOMBRE PUNTO NOMBRE IGUAL PALABRARESERVADA CORCHETEIZQUIERDO NOMBRECOLEECCION CORCHETEDERECHO PUNTOYCOMA

    InsertarUnico -> PALABRARESERVADA NOMBRE PUNTO NOMBRE PUNTO NOMBRE PUNTO NOMBRE IGUAL PALABRARESERVADA CORCHETEIZQUIERDO NOMBRECOLEECCION COMA JSON CORCHETEDERECHO PUNTOYCOMA

    ActualizarUnico -> PALABRARESERVADA NOMBRE PUNTO NOMBRE PUNTO NOMBRE PUNTO NOMBRE IGUAL PALABRARESERVADA CORCHETEIZQUIERDO NOMBRECOLEECCION COMA JSON COMA JSON CORCHETEDERECHO PUNTOYCOMA

    EliminarUnico -> PALABRARESERVADA NOMBRE PUNTO NOMBRE PUNTO NOMBRE PUNTO NOMBRE IGUAL PALABRARESERVADA CORCHETEIZQUIERDO NOMBRECOLEECCION COMA JSON CORCHETEDERECHO PUNTOYCOMA

    BuscarUnico -> PALABRARESERVADA NOMBRE PUNTO NOMBRE PUNTO NOMBRE PUNTO NOMBRE IGUAL PALABRARESERVADA CORCHETEIZQUIERDO NOMBRECOLEECCION  CORCHETEDERECHO PUNTOYCOMA

    BuscarTodo -> PALABRARESERVADA NOMBRE PUNTO NOMBRE PUNTO NOMBRE PUNTO NOMBRE IGUAL PALABRARESERVADA CORCHETEIZQUIERDO NOMBRECOLEECCION CORCHETEDERECHO PUNTOYCOMA
```

# Automata Finito Determinista
El autómata finito determinista (DFA) se utiliza para validar la entrada de acuerdo con la gramática definida. El código proporciona métodos para construir y mostrar el DFA.

![automata](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/Automata.png)