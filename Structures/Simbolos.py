# type -> Tipo de la clase asociado una llave TYPE en la tabla de types
# name -> nombre de la variable
# parentContext -> numero al contexto asociado donde fue creado el simbolo
# value -> valor del simbolo
from .Tipos import *

class Simbolo():
    # constructor
    # el default de la inicializacion es nil porque al principio el tipo del simbolo se desconoce por lo que es Null o Nil en compiscript
    # el default del tipo es tipo porque es el general sin embargo se averiguara conforme se vaya recorriendo el visitor
    # el default del ambito es 0 porque es el ambito main o general
    def __init__(self, nombreSimbolo:str="var1", tipo:Tipo=Tipo(), ambito:int=0) -> None:
        # El identificador del simbolo
        self.nombreSimbolo = nombreSimbolo
        # El tipo del simbolo
        self.tipo:Tipo = tipo
        # El ambito en el que esta el simbolo
        self.ambito:int = ambito

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
        
class Funcion(Simbolo):
    def __init__(self, nombreSimbolo: str = "var1", tipo: Tipo = Tipo(), ambito: int = 0) -> None:
        super().__init__(nombreSimbolo, tipo, ambito)
        # Tendran los id's de los parametros para la ejecucion, por lo que es una lista con str's
        self.parametros = [] 
        # La variable de retorno en caso de que no tenga return retorna un Nil por ende se va a ir generando un nil default que sera actualizado en tiempo de ejecucion
        self.variableRetorno = Nil()
    # Aniadir el contexto o el arbol es necesario para recorrer en tiempo de ejecucion
    def aniadirContexto(self, ctx):
        self.contexto = ctx
    def aniadirParametro(self, parametro):
        self.parametros.append(parametro)

class Metodo(Funcion):
    def __init__(self, nombreSimbolo: str = "var1", tipo: Tipo = Tipo(), ambito: int = 0, parametros=[]) -> None:
        super().__init__(nombreSimbolo, tipo, ambito)
        # Tendran los id's de los parametros para la ejecucion, por lo que es una lista con str's
        self.parametros = [] 
        # La variable de retorno en caso de que no tenga return retorna un Nil por ende se va a ir generando un nil default que sera actualizado en tiempo de ejecucion
        self.variableRetorno = Nil()
        
# Esto nos servira para funciones ya que asi podemos ingresar los parametros de una funcion
class Parametro(Simbolo):
    def __init__(self, nombreSimbolo: str = "var1", tipo: Tipo = Tipo(), ambito: int = 0, inicializador:Tipo=Nil, funcionPertenece:str="") -> None:
        super().__init__(nombreSimbolo, tipo, ambito)
        # Sirve para verificar que el parametro tipo esperado inicializado es el esperado
        self.inicializacion = inicializador
        # Para definir a que funcion pertenece este parametro
        self.perteneceVariable = funcionPertenece
        
    def definirInicializador(self, inicializador:Tipo):
        self.inicializador = inicializador
        
# Variable es una clase para definir cualquier variable independiente de su tipo
# Estas variables su tipo sera determinado por el valor al ser compiscript tipado dinamico
class Variable(Simbolo):
    def __init__(self, nombreSimbolo: str = "var1", tipo: Tipo = Tipo(), ambito: int = 0, inicializador:Tipo=Nil) -> None:
        super().__init__(nombreSimbolo, tipo, ambito)
        # Inicializacion de la variable, sirve para comprobar que el inicializado es el mismo que el esperado
        self.inicializador:Tipo = inicializador
    
    def definirInicializador(self, inicializador:Tipo):
        self.inicializador = inicializador
    
    def redefinirTipo(self, tipo:Tipo):
        self.tipo = tipo