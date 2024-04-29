from Abstract.Abstract import Expression

class Errores(Expression):
    contador = 0
    def __init__(self, tipo,lexema, mensaje, fila, columna):
        self.contador = Errores.contador
        self.lexema = lexema
        self.tipo = tipo
        self.mensaje = mensaje
        super().__init__(fila, columna)
        Errores.contador += 1

    def operar(self, no):
        lex = "Error: " + self.lexema
        return lex

    def getColumna(self):
        return super().getColumna()

    def getFila(self):
        return super().getFila()