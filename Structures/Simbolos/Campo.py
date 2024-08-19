from Simbolo import *
from Structures.Tipos.Tipo import Tipo

# Esto nos servira para clases ya que asi se desglosan las clases en campos (atributos) y funciones (metodos)
class Campo(Simbolo):
    def __init__(self, nombreSimbolo, valor, tipo: Tipo, ambito: int, inicializador:Tipo=Nil, nombreVariable:str="") -> None:
        super().__init__(nombreSimbolo, valor, tipo, ambito)
        # Sirve para verificar que el campo tipo esperado inicializado es el esperado
        self.inicializacion = inicializador
        # Para definir a que variable pertenece este campo o atributo
        self.perteneceVariable = nombreVariable
        