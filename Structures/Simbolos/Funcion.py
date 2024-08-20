from .Simbolo import *
from Structures.Tipos.Tipo import Tipo

# Funcion es una clase para definir las funciones
# Esta funcion sera construida a partir del visitor
class Funcion(Simbolo):
    def __init__(self, nombreSimbolo: str = "var1", tipo: Tipo = Tipo(), ambito: int = 0) -> None:
        super().__init__(nombreSimbolo, tipo, ambito)
        # Tendran los id's de los parametros para la ejecucion, por lo que es una lista con str's
        self.parametros = [] 
        # La variable de retorno en caso de que no tenga return retorna un Nil por ende se va a ir generando un nil default que sera actualizado en tiempo de ejecucion
        self.variableRetorno = Nil()
    # Aniadir el contexto o el arbol es necesario para recorrer en tiempo de ejecucion
    def aniadirContexto(self, ctx):
        self.contexto = ctx
    def aniadirParametro(self, parametro):
        self.parametros.append(parametro)
    