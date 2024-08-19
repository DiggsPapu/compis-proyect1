from Simbolo import *
from Structures.Tipos.Tipo import Tipo

# Funcion es una clase para definir las funciones
# Esta funcion sera construida a partir del visitor
class Funcion(Simbolo):
    def __init__(self, nombreSimbolo, valor, tipo: Tipo, ambito: int, parametros=[]) -> None:
        super().__init__(nombreSimbolo, valor, tipo, ambito)
        # Tendran los id's de los parametros para la ejecucion, por lo que es una lista con str's
        self.parametros = parametros    
    # Definir el tipo o como es el retorno de la funcion, es str porque es la llave de la variable retorno para comparar en ejecucion, 
    # podriamos poner un parametro como este retorno, al fin y al cabo solo se usan en funciones.
    def definirRetorno(self, variableRetorno:str):
        self.variableRetorno = variableRetorno
    