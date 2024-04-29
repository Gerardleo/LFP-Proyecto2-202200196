
from Error.Errores import *
from Abstract.Abstract  import Expression


class Funcion(Expression):

    def __init__(self, crear, nombre, igual, nueva, crear2, fila, columna):
        self.crear = crear
        self.nombre = nombre
        self.igual = igual
        self.nueva = nueva
        self.crear2 = crear2
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self):
        if self.crear == 'CrearBD':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'nueva':
                        if self.crear2 == 'CrearBD()':
                            return 'use(' + self.nombre + ');',None,self.getFila(), self.getColumna(),None
                        else:
                            return None,' falta la palabra reservada CrearDB()',self.getFila(), self.getColumna(),self.crear2
                    else:
                        return None,' Falta la palabra reservada nueva',self.getFila(), self.getColumna(),self.nueva
                else:
                    return None,' Falta el simbolo =',self.getFila(), self.getColumna(),self.igual
            else:
                return None,' Falta el nombre de la base de datos',self.getFila(), self.getColumna(),self.nombre
            
        elif self.crear == 'EliminarBD':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'nueva':
                        if self.crear2 == 'EliminarBD()':
                            return 'db.dropDatabase();',None,self.getFila(), self.getColumna(),None
                        else:
                            return None,' falta la palabra reservada EliminarBD()',self.getFila(), self.getColumna(),self.crear2
                    else:
                        return None,' Falta la palabra reservada nueva',self.getFila(), self.getColumna(),self.nueva
                else:
                    return None,' Falta el simbolo =',self.getFila(), self.getColumna(),self.igual
            else:
                return None,'Falta el nombre de la base de datos',self.getFila(), self.getColumna(),self.nombre
        else:
            return None, 'Nombre incorrecto',self.getFila(), self.getColumna(),self.crear
 

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
