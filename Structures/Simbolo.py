# type -> Tipo de la clase asociado una llave TYPE en la tabla de types
# name -> nombre de la variable
# parentContext -> numero al contexto asociado donde fue creado el simbolo
# value -> valor del simbolo
from Structures.Tipos.Tipo import *

class Symbol():
    # constructor
    def __init__(self, nombreSimbolo, valor, tipo:Tipo) -> None:
        self.nombreSimbolo = nombreSimbolo
        self.valor = valor
        self.tipo:Tipo = tipo