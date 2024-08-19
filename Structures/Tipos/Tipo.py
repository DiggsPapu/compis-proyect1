# Key -> Nombre del tipo por ejemplo INT para entero
# Value -> Clase del tipo por ejemplo la clase int que defina que puede o que no puede hacer el tipo

class Tipo():
    def __init__(self, nombreTipo="tipo", valor="tipo") -> None:
        self.nombreTipo = nombreTipo
        self.valor = valor
    def __str__(self) -> str:
        return "tipo"
# Operadores universales que todos los tipos usan
    # Comparacion
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
    
# Operaciones usados solo por booleanos
    # and
    def opAnd(val1, val2):
        pass
    # or
    def opOr(val1, val2):
        pass
    # !
    def opNo(val1, val2):
        pass
# Operadores solo usados por numeros y en el caso de la suma por cadenas
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