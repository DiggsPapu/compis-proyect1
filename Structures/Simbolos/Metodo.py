from Funcion import *
from Structures.Simbolos.Simbolo import Tipo
from Structures.Tipos.Tipo import Tipo

class Metodo(Funcion):
    def __init__(self, nombreSimbolo: str = "var1", tipo: Tipo = Tipo(), ambito: int = 0, parametros=[]) -> None:
        super().__init__(nombreSimbolo, tipo, ambito, parametros)
    
    