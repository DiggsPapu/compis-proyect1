# Contexto
# Id que identifique al contexto
# ambitosHijos, para saber cuales son los ambitos hijos
from .BasicStructures import *
from .Tipos import *

class Ambito():
    def __init__(
        self, 
        identificador:int, 
        tablaDeSimbolos:HashMap,
        tablaDeTipos: HashMap
        ) -> None:
        self.identificadorAmbito = identificador
        self.tablaDeSimbolos = tablaDeSimbolos
        self.tablaDeTipos = tablaDeTipos
        # Poner los tipos basicos
        self.tablaDeTipos.replaceMap({"numero": Numero(), "booleano":Booleano(), "cadena": Cadena(), "nil":Nil(), "definidoPorUsuario":DefinidoPorUsuario(), "tipo":Tipo(), "tipoFuncion":TipoFuncion()})
        self.ambitosHijos = set()
    
    # Aniadir contextos hijos
    def aniadirContextoHijo(self, hijo:int):
        self.ambitosHijos.add(hijo)
        
    # Eliminar contextos hijos, por ejemplo, cuando se termina de ejecutar
    def eliminarContextoHijo(self, hijo:int):
        self.ambitosHijos.remove(hijo)