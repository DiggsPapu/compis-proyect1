# type -> Tipo de la clase asociado una llave TYPE en la tabla de types
# name -> nombre de la variable
# parentContext -> numero al contexto asociado donde fue creado el simbolo
# value -> valor del simbolo
from Structures.Tipos.Tipo import *
from Structures.Tipos.Nil import *

class Simbolo():
    # constructor
    # el default de la inicializacion es nil porque al principio el tipo del simbolo se desconoce por lo que es Null o Nil en compiscript
    # el default del tipo es tipo porque es el general sin embargo se averiguara conforme se vaya recorriendo el visitor
    # el default del ambito es 0 porque es el ambito main o general
    def __init__(self, nombreSimbolo:str="var1", tipo:Tipo=Tipo(), ambito:int=0) -> None:
        # El identificador del simbolo
        self.nombreSimbolo = nombreSimbolo
        # El tipo del simbolo
        self.tipo:Tipo = tipo
        # El ambito en el que esta el simbolo
        self.ambito:int = ambito