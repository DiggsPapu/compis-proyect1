from Structures.Tipos.Tipo import *

class Numero(Tipo):
    def __init__(self, nombreTipo="numero", valor="numero") -> None:
        super().__init__(nombreTipo, valor)
    def __str__(self) -> str:
        return "numero"
    # >
    def mayorQue(val1, val2):
        pass
    # <
    def menorQue(val1, val2):
        pass
    # >=
    def mayorIgualQue(val1, val2):
        pass
    # <=
    def menorIgualQue(val1, val2):
        pass
    # ==
    def igualQue(val1, val2):
        pass
    # !=
    def diferenteQue(val1, val2):
        pass
    # +
    def suma(val1, val2):
        pass
    # -
    def resta(val1, val2):
        pass
    # *
    def multiplicacion(val1, val2):
        pass
    # /
    def division(val1, val2):
        pass