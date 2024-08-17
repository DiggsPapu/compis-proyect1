# Contexto
# Id que identifique al contexto
# set de parent context para que se tengan los parent contexts
# set de child context para tener todos los contextos hijos
class Contexto():
    def __init__(self, id:int, contextoPadre:int, contextoHijo:int) -> None:
        self.id = id
        self.parentContext = set(contextoPadre)
        self.childContext = set(contextoHijo)