
from Error.Errores import *
from Abstract.Abstract  import Expression


class FuncionUnParametros(Expression):

    def __init__(self, crear, nombre, igual, nueva, crear2, nombreColeccion,fila, columna):
        self.crear = crear
        self.nombre = nombre
        self.igual = igual
        self.nueva = nueva
        self.crear2 = crear2
        self.nombreColeccion = nombreColeccion
        super().__init__(fila, columna)

    def operar(self, arbol):
        pass

    def ejecutarT(self):
        if self.crear == 'CrearColeccion':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'nueva':
                        if self.crear2 == 'CrearColeccion(':
                            if self.nombreColeccion != None:
                                return 'db.createCollection("' + self.nombreColeccion + '");',None,self.getFila(), self.getColumna(),None
                            else:
                                return None,' Falta el nombre de la coleccion',self.getFila(), self.getColumna(),self.nombreColeccion
                        else:
                            return None,' falta la palabra reservada CrearColeccion(',self.getFila(), self.getColumna(),self.crear2
                    else:
                        return None,' Falta la palabra reservada nueva',self.getFila(), self.getColumna(),self.nueva
                else:
                    return None,' Falta el simbolo =',self.getFila(), self.getColumna(),self.igual
            else:
                return None,' Falta el nombre de la base de datos',self.getFila(), self.getColumna(),self.nombre
        elif self.crear == 'EliminarColeccion':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'nueva':
                        if self.crear2 == 'EliminarColeccion(':
                            if self.nombreColeccion != None:
                                return 'db.' + self.nombreColeccion + '.drop();',None,self.getFila(), self.getColumna(),None
                            else:
                                return None,' Falta el nombre de la coleccion',self.getFila(), self.getColumna(),self.nombreColeccion
                        else:
                            return None,' falta la palabra reservada EliminarColeccion(',self.getFila(), self.getColumna(),self.crear2
                    else:
                        return None,' Falta la palabra reservada nueva',self.getFila(), self.getColumna(),self.nueva
                else:
                    return None,' Falta el simbolo =',self.getFila(), self.getColumna(),self.igual
            else:
                return None,' Falta el nombre de la base de datos',self.getFila(), self.getColumna(),self.nombre
            
        
        elif self.crear == 'BuscarTodo':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'nueva':
                        if self.crear2 == 'BuscarTodo(':
                            if self.nombreColeccion != None:
                                return 'db.' + self.nombreColeccion + '.find();',None,self.getFila(), self.getColumna(),None
                            else:
                                return None,' Falta el nombre de la coleccion',self.getFila(), self.getColumna(),self.nombreColeccion
                        else:
                            return None,' falta la palabra reservada BuscarTodo(',self.getFila(), self.getColumna(),self.crear2
                    else:
                        return None,' Falta la palabra reservada nueva',self.getFila(), self.getColumna(),self.nueva
                else:
                    return None,' Falta el simbolo =',self.getFila(), self.getColumna(),self.igual
            else:
                return None,' Falta el nombre de la base de datos',self.getFila(), self.getColumna(),self.nombre
        elif self.crear == 'BuscarUnico':
            if self.nombre != None:
                if self.igual == '=':
                    if self.nueva == 'nueva':
                        if self.crear2 == 'BuscarUnico(':
                            if self.nombreColeccion != None:
                                return 'db.' + self.nombreColeccion + '.findOne();',None,self.getFila(), self.getColumna(),None
                            else:
                                return None,' Falta el nombre de la coleccion',self.getFila(), self.getColumna(),self.nombreColeccion
                        else:
                            return None,' falta la palabra reservada BuscarUnico(',self.getFila(), self.getColumna(),self.crear2
                    else:
                        return None,' Falta la palabra reservada nueva',self.getFila(), self.getColumna(),self.nueva
                else:
                    return None,' Falta el simbolo =',self.getFila(), self.getColumna(),self.igual
            else:
                return None,' Falta el nombre de la base de datos',self.getFila(), self.getColumna(),self.nombre
        else:
            return None, 'Nombre incorrecto',self.getFila(), self.getColumna(),self.crear

    def getFila(self):
        return super().getFila()

    def getColumna(self):
        return super().getColumna()
