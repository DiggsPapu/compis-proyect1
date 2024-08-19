# Contexto
# Id que identifique al contexto
# set de parent context para que se tengan los parent contexts
# set de child context para tener todos los contextos hijos
class Contexto():
    def __init__(
        self, 
        identificador:int, 
        # contextoPadre:int, 
        contextoHijo:int
        ) -> None:
        self.identificadorContexto = identificador
        # Es redundante
        # self.parentContext = set(contextoPadre)
        self.contextosHijos = set(contextoHijo)
    
    # Aniadir contextos hijos
    def aniadirContextoHijo(self, hijo:int):
        self.contextosHijos.add(hijo)
        
    # Eliminar contextos hijos, por ejemplo, cuando se termina de ejecutar
    def eliminarContextoHijo(self, hijo:int):
        self.contextosHijos.remove(hijo)    