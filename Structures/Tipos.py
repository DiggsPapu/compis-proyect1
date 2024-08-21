# Key -> Nombre del tipo por ejemplo INT para entero
# Value -> Clase del tipo por ejemplo la clase int que defina que puede o que no puede hacer el tipo

from Structures.BasicStructures import HashMap


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


class Cadena(Tipo):
    def __init__(self, nombreTipo="cadena", valor="cadena") -> None:
        super().__init__(nombreTipo, valor)
    def __str__(self) -> str:
        return "cadena"
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


class DefinidoPorUsuario(Tipo):
    def __init__(self, nombreTipo="tipo", valor="tipo") -> None:
        super().__init__(nombreTipo, valor)
        self.metodosCtx = HashMap()
    
    def __str__(self) -> str:
        return self.nombreTipo
        
    def initContext(self, parametros,ctx):
        self.initParams = parametros
        self.init = ctx
    
    # Se aniade el contexto del metodo para que se genere cada vez que se quiera ejecutar
    def aniadirMetodos(self, metodoNombre, ctx):
        self.metodosCtx.put(metodoNombre, ctx)
        
class Nil(Tipo):
    def __init__(self, nombreTipo="nil", valor="nil") -> None:
        super().__init__(nombreTipo, valor)
    def __str__(self) -> str:
        return "nil"
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

class TipoFuncion(Tipo):
    def __init__(self, nombreTipo="tipo", valor="tipo") -> None:
        super().__init__(nombreTipo, valor)
        
    def __str__(self) -> str:
        return "funcion"    
    