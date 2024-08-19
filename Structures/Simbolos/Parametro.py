from Simbolo import *
from Structures.Tipos.Tipo import Tipo

# Esto nos servira para funciones ya que asi podemos ingresar los parametros de una funcion
class Parametro(Simbolo):
    def __init__(self, nombreSimbolo, valor, tipo: Tipo, ambito: int, inicializador:Tipo=Nil, nombreVariable:str="") -> None:
        super().__init__(nombreSimbolo, valor, tipo, ambito)
        # Sirve para verificar que el parametro tipo esperado inicializado es el esperado
        self.inicializacion = inicializador
        # Para definir a que funcion pertenece este parametro
        self.perteneceVariable = nombreVariable
        
    def definirInicializador(self, inicializador:Tipo):
        self.inicializador = inicializador