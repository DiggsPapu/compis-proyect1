# Contexto
# Id que identifique al contexto
# ambitosHijos, para saber cuales son los ambitos hijos
from  Structures.HashMap import *

class Ambito():
    def __init__(
        self, 
        identificador:int, 
        tablaDeSimbolos:HashMap
        ) -> None:
        self.identificadorAmbito = identificador
        self.tablaDeSimbolos = tablaDeSimbolos
        self.ambitosHijos = set()
    
    # Aniadir contextos hijos
    def aniadirContextoHijo(self, hijo:int):
        self.ambitosHijos.add(hijo)
        
    # Eliminar contextos hijos, por ejemplo, cuando se termina de ejecutar
    def eliminarContextoHijo(self, hijo:int):
        self.ambitosHijos.remove(hijo)