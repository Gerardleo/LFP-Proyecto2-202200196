from Instrucciones.Funcion import *
from Instrucciones.FuncionDosParametros import *
from Instrucciones.FuncionUnParametros import *
from Instrucciones.FuncionTresParametros import *
from Error.Errores import *
from Abstract.Lexema import *

global n_linea
global n_columna
global instrucciones
global lista_lexemas
global lista_errores

n_linea = 1
n_columna = 1
lista_lexemas = []
instrucciones = []
lista_erroresLex = []
listaErroresSin = []

palabras_reservadas = {"CrearDB": "CrearDB",
                       "=": "IGUAL",
                       ",": "COMA",
                       ";": "PUNTOYCOMA",
                       "*/": "COMENTARIO_MULTILINEA",
                       "---": "COMENTARIO",
                        "(": "PARENTESISIZQ",
                        ")": "PARENTESISDER"}
def instruccion(cadena):
    global n_linea, n_columna, lista_lexemas, lista_erroresLex, listaErroresSin
    lexema = ''
    puntero = 0
    lista_lexemas = []
    lista_erroresLex = []
    listaErroresSin = []
    n_linea = 1
    n_columna = 1


    while cadena:
        char = cadena[puntero]
        puntero += 1

        if char.isupper() or char.islower():       #! leemos nuestra cadena y al encontrar " que habre empieza a crear el token
            lexema, cadena = armar_lexema(cadena)
            if lexema and cadena:
                n_columna += 1
                #Armar lexema como clase
                l = Lexema('STRING',lexema, n_linea, n_columna)
                lista_lexemas.append(l)  #! Agregamos los lexemas a la lista_lexema
                n_columna += len(lexema) + 1
                puntero = 0

        elif char == '{':
            lexema, cadena = armar_lexema_Json(cadena)
            if lexema and cadena:
                n_columna += 1
                #Armar lexema como clase
                l = Lexema('JSON',lexema, n_linea, n_columna)
                lista_lexemas.append(l)

        elif char in palabras_reservadas:
            #! Armamos lexema como clase
            c = Lexema(palabras_reservadas[char],char, n_linea, n_columna)

            lista_lexemas.append(c)
            cadena = cadena[1:]
            puntero = 0
            n_columna += 1

        elif char =="\t":
            n_columna += 4
            cadena = cadena[4:]
            puntero = 0
        elif char == "\n":
            cadena = cadena[1:]
            puntero = 0
            n_linea += 1
            n_columna = 1
        elif char == ' ' or char == '\r':
            n_columna += 1
            cadena = cadena[1:]
            puntero = 0
        elif char == '/':
            while cadena[puntero] != "/":
                puntero =0
                cadena = cadena[1:]
                if cadena[puntero] == "\n":
                    n_linea += 1
                    n_columna = 1 
            cadena = cadena[1:]
            puntero = 0
        elif char == '-':
            contador = 0
            while contador < 2 :
                if cadena[puntero] == '-':
                    contador += 1
                puntero = 0

            if contador == 2:
                while cadena[puntero] != "\n":
                    cadena = cadena[1:]
                    puntero += 0
                    n_columna += 1
                n_linea += 1  # Aumenta la línea al final del comentario de varias líneas
                n_columna = 1  # Restablece la columna al inicio de la nueva línea
            else:
                listaErroresSin.append(Errores("Sintatico",char,"No se cerro el comentario", n_linea, n_columna))
        else:
            if char == '"' or char == "}":
                cadena = cadena[1:]
                puntero = 0
                n_columna += 1
            else:
                lista_erroresLex.append(Errores("Lexico",char,"Caracter Desconocido", n_linea, n_columna))
                cadena = cadena[1:]
                puntero = 0
                n_columna += 1


    return lista_lexemas,lista_erroresLex,listaErroresSin

def armar_lexema(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        if char == ' ' or char == ';' or char == '"':
            return lexema, cadena[len(puntero):]    #! si encuentra una  " termino de leer el token
        else:
            lexema += char   #! creamos nuestros Token
    return None, None

def armar_lexema_Json(cadena):
    global n_linea
    global n_columna
    global lista_lexemas
    lexema = ''
    puntero = ''

    for char in cadena:
        puntero += char
        valor = cadena[len(puntero) + 1]
        if char == '}':
            lexema += char
            return lexema, cadena[len(puntero):]    #! si encuentra una  " termino de leer el token
        else:
            lexema += char   #! creamos nuestros Token
    return None, None



def operar():
    global lista_lexemas
    global instrucciones
    while lista_lexemas:
        lexema = lista_lexemas.pop(0)
        if lexema.operar(None) == 'CrearBD':
            nombredb = lista_lexemas.pop(0)
            igualdb = lista_lexemas.pop(0)
            nuevadb = lista_lexemas.pop(0)
            creardb2 = lista_lexemas.pop(0)
            func = Funcion(lexema.lexema, nombredb.lexema, igualdb.lexema, nuevadb.lexema, creardb2.lexema, lexema.getFila(), lexema.getColumna())
            return func  # Devuelve func cuando se crea una base de datos
        elif lexema.operar(None) == 'InsertarUnico':
            nombredb = lista_lexemas.pop(0)
            igualdb = lista_lexemas.pop(0)
            nuevadb = lista_lexemas.pop(0)
            insertardb2 = lista_lexemas.pop(0)
            nombredb2 = lista_lexemas.pop(0)
            comadb = lista_lexemas.pop(0)
            jsondb = lista_lexemas.pop(0)
            parentesisdb = lista_lexemas.pop(0)
            puntoycomadb = lista_lexemas.pop(0)
            func = FuncionDosParametros(lexema.lexema, nombredb.lexema, igualdb.lexema, nuevadb.lexema, insertardb2.lexema, nombredb2.lexema, comadb.lexema, jsondb.lexema, parentesisdb.lexema, puntoycomadb.lexema, lexema.getFila(), lexema.getColumna())
            return func  # Devuelve func cuando se crea una base de datos
        elif lexema.operar(None) == 'EliminarBD':
            nombredb = lista_lexemas.pop(0)
            igualdb = lista_lexemas.pop(0)
            nuevadb = lista_lexemas.pop(0)
            creardb2 = lista_lexemas.pop(0)
            func = Funcion(lexema.lexema, nombredb.lexema, igualdb.lexema, nuevadb.lexema, creardb2.lexema, lexema.getFila(), lexema.getColumna())
            return func  # Devuelve func cuando se crea una base de datos
        elif lexema.operar(None) == 'EliminarUnico':
            nombredb = lista_lexemas.pop(0)
            igualdb = lista_lexemas.pop(0)
            nuevadb = lista_lexemas.pop(0)
            insertardb2 = lista_lexemas.pop(0)
            nombredb2 = lista_lexemas.pop(0)
            comadb = lista_lexemas.pop(0)
            jsondb = lista_lexemas.pop(0)
            parentesisdb = lista_lexemas.pop(0)
            puntoycomadb = lista_lexemas.pop(0)
            func = FuncionDosParametros(lexema.lexema, nombredb.lexema, igualdb.lexema, nuevadb.lexema, insertardb2.lexema, nombredb2.lexema, comadb.lexema, jsondb.lexema, parentesisdb.lexema, puntoycomadb.lexema, lexema.getFila(), lexema.getColumna())
            return func  # Devuelve func cuando se crea una base de datos
        elif lexema.operar(None) == 'CrearColeccion':
            nombredb = lista_lexemas.pop(0)
            igualdb = lista_lexemas.pop(0)
            nuevadb = lista_lexemas.pop(0)
            creardb2 = lista_lexemas.pop(0)
            nombreColeccion = lista_lexemas.pop(0)
            func = FuncionUnParametros(lexema.lexema, nombredb.lexema, igualdb.lexema, nuevadb.lexema, creardb2.lexema,nombreColeccion.lexema, lexema.getFila(), lexema.getColumna())
            return func  # Devuelve func cuando se crea una base de datos
        elif lexema.operar(None) == 'EliminarColeccion':
            nombredb = lista_lexemas.pop(0)
            igualdb = lista_lexemas.pop(0)
            nuevadb = lista_lexemas.pop(0)
            creardb2 = lista_lexemas.pop(0)
            nombreColeccion = lista_lexemas.pop(0)
            func = FuncionUnParametros(lexema.lexema, nombredb.lexema, igualdb.lexema, nuevadb.lexema, creardb2.lexema,nombreColeccion.lexema, lexema.getFila(), lexema.getColumna())
            return func  # Devuelve func cuando se crea una base de datos
        elif lexema.operar(None) == 'BuscarTodo':
            nombredb = lista_lexemas.pop(0)
            igualdb = lista_lexemas.pop(0)
            nuevadb = lista_lexemas.pop(0)
            creardb2 = lista_lexemas.pop(0)
            nombreColeccion = lista_lexemas.pop(0)
            func = FuncionUnParametros(lexema.lexema, nombredb.lexema, igualdb.lexema, nuevadb.lexema, creardb2.lexema,nombreColeccion.lexema, lexema.getFila(), lexema.getColumna())
            return func  # Devuelve func cuando se crea una base de datos
        elif lexema.operar(None) == 'BuscarUnico':
            nombredb = lista_lexemas.pop(0)
            igualdb = lista_lexemas.pop(0)
            nuevadb = lista_lexemas.pop(0)
            creardb2 = lista_lexemas.pop(0)
            nombreColeccion = lista_lexemas.pop(0)
            func = FuncionUnParametros(lexema.lexema, nombredb.lexema, igualdb.lexema, nuevadb.lexema, creardb2.lexema,nombreColeccion.lexema, lexema.getFila(), lexema.getColumna())
            return func  # Devuelve func cuando se crea una base de datos
        elif lexema.operar(None) == 'ActualizarUnico':
            nombredb = lista_lexemas.pop(0)
            igualdb = lista_lexemas.pop(0)
            nuevadb = lista_lexemas.pop(0)
            insertardb2 = lista_lexemas.pop(0)
            nombredb2 = lista_lexemas.pop(0)
            comadb = lista_lexemas.pop(0)
            jsondb = lista_lexemas.pop(0)
            jsondb2 = lista_lexemas.pop(0)
            parentesisdb = lista_lexemas.pop(0)
            puntoycomadb = lista_lexemas.pop(0)
            func = FuncionTresParametros(lexema.lexema, nombredb.lexema, igualdb.lexema, nuevadb.lexema, insertardb2.lexema, nombredb2.lexema, comadb.lexema, jsondb.lexema, jsondb2.lexema, parentesisdb.lexema, puntoycomadb.lexema, lexema.getFila(), lexema.getColumna())
            return func  # Devuelve func cuando se crea una base de datos


    return None  # Devuelve None si no se realiza ninguna operación

def operar_():
    global instrucciones
    temp_instrucciones = []
    while True:
        operacion = operar()

        if operacion:
            temp_instrucciones.append(operacion)
        else:
            break
    instrucciones = temp_instrucciones

    return instrucciones

def getErrores():
    global lista_errores
    return lista_errores


