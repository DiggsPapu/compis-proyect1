from Simbolo import *
from Structures.Tipos.Tipo import Tipo

# Variable es una clase para definir cualquier variable independiente de su tipo
# Estas variables su tipo sera determinado por el valor al ser compiscript tipado dinamico
class Variable(Simbolo):
    def __init__(self, nombreSimbolo, valor, tipo: Tipo, ambito: int, inicializador:Tipo=Nil) -> None:
        super().__init__(nombreSimbolo, valor, tipo, ambito)
        # Inicializacion de la variable, sirve para comprobar que el inicializado es el mismo que el esperado
        self.inicializador:Tipo = inicializador
    
    def definirInicializador(self, inicializador:Tipo):
        self.inicializador = inicializador
    
    def redefinirTipo(self, tipo:Tipo):
        self.tipo = tipo
    