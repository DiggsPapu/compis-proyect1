from .Tipo import *

class TipoFuncion(Tipo):
    def __init__(self, nombreTipo="tipo", valor="tipo") -> None:
        super().__init__(nombreTipo, valor)
        
    def __str__(self) -> str:
        return "funcion"    
    