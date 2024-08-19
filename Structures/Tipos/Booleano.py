from Structures.Tipos.Tipo import *

class Booleano(Tipo):
    def __init__(self, nombreTipo="booleano", valor="booleano") -> None:
        super().__init__(nombreTipo, valor)
    
    def __str__(self) -> str:
        return "booleano"
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
    # and
    def opAnd(val1, val2):
        pass
    # or
    def opOr(val1, val2):
        pass
    # !
    def opNo(val1, val2):
        pass