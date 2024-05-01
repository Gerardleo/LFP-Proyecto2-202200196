# Proyecto No.2 - Lenguajes Formales y de Programacion

# Manual de Usuario - Lectura de Archivos lfp




**Nombre:** Gerardo Leonel Ortiz Tobar
**Carnet:** 202200196


# Interfaz grafica (interfaz.py)
Se presenta la interfaz principal de la lectura de archivos lfp, la cual permite abrir un archivo de texto, analizarlo y generar reportes de los tokens, errores y arbol de derivacion.
![Menu](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/Interfaz.png)


Se presentan las siguientes opciones de archivo:

- abrir: Permite abrir un archivo de formato bizdata
- guardar: Permite guardar el archivo que se esta utilizando
- analizar archivo: Permite analizar el archivo que se esta utilizando
- limpiar: Permite limpiar toda la informacion que se encuentra en el cuadro de texto y en la aplicacion
- Salir: Permite cerrar la aplicacion

![abrir](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/abrir.png)

La funcion Abrir se encarga de abrir el archivo y mostrarlo en el cuadro de texto

![guardar](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/guardar.png)

La funcion Guardar se encarga de guardar el archivo que se esta utilizando

![analizar](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/analizar.png)

La funcion Analizar archivo se encarga de analizar el archivo que se esta utilizando y mostrar los resultos que se encuentren
![salir](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/salir%20(2).png)


La funcion Salir se encarga de cerrar la aplicacion

![limpiar](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/limpiar.png)
La funcion Limpiar se encarga de limpiar toda la informacion que se encuentra en la aplicacion

Se presentan las siguientes opciones de Reportes:

- Reporte de Tokens: Permite generar el reporte de tokens
- Reporte de Errores Lexicos: Permite generar el reporte de errores
- Reporte de Errores Sintacticos: Permite generar el reporte de errores

![reporteTokens](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/tokens.png)

La funcion Reporte de Tokens se encarga de generar el reporte de tokens en formato html


![reporteLexicos](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/lexico.png)

La funcion Reporte de Errores Lexicos se encarga de generar el reporte de errores en formato html

![reporteSintatico](https://github.com/Gerardleo/LFP-Proyecto2-202200196/blob/main/img_reportes/sintaticos.png)

La funcion Reporte de Errores Sintaxticos se encarga de generar el reporte de errores en formato html



<br>
<br>
<br>

# Analizadores
Se presentan los analizadores que se utilizaron para poder analizar el archivo de texto
## Analizador Lexico
El analizador lexico se encarga de analizar el archivo de texto y separarlo en tokens, para esto se utilizo la libreria ply.lex, la cual permite crear tokens con expresiones regulares, ademas de poder ignorar los comentarios y los espacios en blanco.

## Analizador Sintactico 
El analizador sintactico se encarga de analizar los tokens que se generaron en el analizador lexico, para esto se utilizo la libreria ply.yacc, la cual permite crear reglas de produccion para poder analizar los tokens y generar el arbol de derivacion.

<br>
<br>
<br>

# Conclusiones
El proyecto fue de gran ayuda para poder entender el funcionamiento de los analizadores lexicos y sintacticos, ademas de poder entender el funcionamiento de las expresiones regulares y como se pueden utilizar para poder analizar un archivo de texto.