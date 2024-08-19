from Simbolo import *
from Structures.Tipos.Tipo import Tipo

# Esto nos servira para clases ya que asi se desglosan las clases en campos (atributos) y funciones (metodos)
class Campo(Simbolo):
    def __init__(self, nombreSimbolo: str = "var1", tipo: Tipo = Tipo(), ambito: int = 0, inicializador:Tipo=Nil, nombreVariable:str="") -> None:
        super().__init__(nombreSimbolo, tipo, ambito)
        # Sirve para verificar que el campo tipo esperado inicializado es el esperado
        self.inicializacion = inicializador
        # Para definir a que variable pertenece este campo o atributo
        self.perteneceVariable = nombreVariable
        
    def definirInicializador(self, inicializador:Tipo):
        self.inicializador = inicializador