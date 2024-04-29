from Error.Errores import *
from Abstract.Abstract  import Expression


class FuncionTresParametros(Expression):

    def __init__(self, insertar, nombre, igual, nueva, insertar2, nombre2 ,coma, jsondb,jsondb2,parentesis,puntoycoma, fila, columna):
        self.insertar = insertar
        self.nombre = nombre
        self.igual = igual
        self.nueva = nueva
        self.insertar2 = insertar2
        self.nombreColeccion = nombre2
        self.coma = coma
        self.jsondb = jsondb
        self.jsondb2 = jsondb2
        self.parentesis = parentesis
        self.puntoycoma = puntoycoma   
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self):
        if self.insertar == 'ActualizarUnico':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'nueva':
                        if self.insertar2 == 'ActualizarUnico(':
                            if self.nombreColeccion != None:
                                if self.coma == ',':
                                    if self.jsondb != None:
                                            if self.jsondb2 != None:
                                                if self.parentesis == ')':
                                                    if self.puntoycoma == ';':
                                                        return 'db.'+ self.nombreColeccion + '.updateOne(' + self.jsondb + ',' + self.jsondb2 + ');',None,self.getFila(), self.getColumna(),None
                                                    else:
                                                        return None,' Falta el punto y coma',self.getFila(), self.getColumna(),self.puntoycoma
                                                else:
                                                    return None,' Falta el parentesis de cierre',self.getFila(), self.getColumna(),self.parentesis
                                            else:
                                                return None,' Falta el json2',self.getFila(), self.getColumna(),self.jsondb2
                                    else:
                                        return None,' Falta el json',self.getFila(), self.getColumna(),self.jsondb
                                else:
                                    return None,' Falta la coma',self.getFila(), self.getColumna(),self.coma
                            else:
                                return None,' Falta el nombre de la tabla',self.getFila(), self.getColumna(), self.nombreColeccion
                        else:
                            return None,' Falta la palabra reservada InsertarUnico(',self.getFila(), self.getColumna(),self.insertar2
                    else:
                        return None,' Falta la palabra reservada nueva',self.getFila(), self.getColumna(),self.nueva
                else:
                    return None,' Falta el simbolo =',self.getFila(), self.getColumna(),self.igual
            else:
                return None,' Falta el nombre de la base de datos',self.getFila(), self.getColumna(),self.nombre
            
    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()