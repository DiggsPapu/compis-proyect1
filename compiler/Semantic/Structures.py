# Key -> Nombre del tipo por ejemplo INT para entero
# Value -> Clase del tipo por ejemplo la clase int que defina que puede o que no puede hacer el tipo


import copy
import re

class Tipo():
    def __init__(self, nombreTipo="tipo", valor="tipo") -> None:
        self.nombreTipo = nombreTipo
        self.valor = valor
    def __str__(self) -> str:
        return "tipo"

class Booleano(Tipo):
    def __init__(self, nombreTipo="booleano", valor="") -> None:
        super().__init__(nombreTipo, valor)
    
    def __str__(self) -> str:
        return "booleano"


class Cadena(Tipo):
    def __init__(self, nombreTipo="cadena", valor="") -> None:
        super().__init__(nombreTipo, valor)
    def __str__(self) -> str:
        return "cadena"


class DefinidoPorUsuario(Tipo):
    def __init__(self, nombreTipo="tipo", valor="") -> None:
        super().__init__(nombreTipo, valor)
        self.metodosCtx = HashMap()
        self.init = None
        self.initParams = None
        self.inheritance = None
        
    def __str__(self) -> str:
        return self.nombreTipo
        
    def initContext(self, parametros,ctx):
        self.initParams = parametros
        self.init = ctx
    def setInheritance(self, className):
        self.inheritance = className
    # Se aniade el contexto del metodo para que se genere cada vez que se quiera ejecutar
    def aniadirMetodos(self, metodoNombre, ctx):
        self.metodosCtx.put(metodoNombre, ctx)
        
class Nil(Tipo):
    def __init__(self, nombreTipo="nil", valor="nil") -> None:
        super().__init__(nombreTipo, valor)
    def __str__(self) -> str:
        return "nil"
    
class Numero(Tipo):
    def __init__(self, nombreTipo="numero", valor="numero") -> None:
        super().__init__(nombreTipo, valor)
    def __str__(self) -> str:
        return "numero"

class TipoFuncion(Tipo):
    def __init__(self, nombreTipo="tipo", valor="tipo") -> None:
        super().__init__(nombreTipo, valor)
        
    def __str__(self) -> str:
        return "funcion"    

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
        self.inicializador = inicializador
        # Para definir a que variable pertenece este campo o atributo
        self.perteneceVariable = nombreVariable
    def redefinirTipo(self, tipo:Tipo):
        self.tipo = tipo
        
    def definirInicializador(self, inicializador:Tipo):
        self.inicializador = inicializador
        
class Funcion(Simbolo):
    def __init__(self, nombreSimbolo: str = "var1", tipo: Tipo = Tipo(), ambito: int = 0) -> None:
        super().__init__(nombreSimbolo, tipo, ambito)
        # Tendran los id's de los parametros para la ejecucion, por lo que es una lista con str's
        self.parametros = [] 
        # La variable de retorno en caso de que no tenga return retorna un Nil por ende se va a ir generando un nil default que sera actualizado en tiempo de ejecucion
        self.variableRetorno = []
        self.contexto = None
    # Aniadir el contexto o el arbol es necesario para recorrer en tiempo de ejecucion
    def aniadirContexto(self, ctx):
        self.contexto = ctx
    def aniadirParametro(self, parametro):
        self.parametros.append(parametro)

class Metodo(Funcion):
    def __init__(self, nombreSimbolo: str = "var1", tipo: Tipo = Tipo(), ambito: int = 0) -> None:
        super().__init__(nombreSimbolo, tipo, ambito)
        # Tendran los id's de los parametros para la ejecucion, por lo que es una lista con str's
        self.parametros = [] 
        # La variable de retorno en caso de que no tenga return retorna un Nil por ende se va a ir generando un nil default que sera actualizado en tiempo de ejecucion
        
# Esto nos servira para funciones ya que asi podemos ingresar los parametros de una funcion
class Parametro(Simbolo):
    def __init__(self, nombreSimbolo: str = "var1", tipo: Tipo = Tipo(), ambito: int = 0, inicializador:Tipo=Nil, funcionPertenece:str="") -> None:
        super().__init__(nombreSimbolo, tipo, ambito)
        # Sirve para verificar que el parametro tipo esperado inicializado es el esperado
        self.inicializador = inicializador
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
        
# Esta es la estructura basica para hacer las tablas, de tipos, de simbolos y de contextos

# Tabla de Simbolos
# Key -> tupla type_name para identificar el nombre
# Value -> Symbol

# Tabla de tipos
# Key -> nombre del type por ejemplo INT
# Value -> clase de type

# Tabla de contextos
# Key -> numero del contexto por ejemplo 0 que seria el main
# Value -> Clase contexto
class HashMap:
    def __init__(self):
        self.map = {}
    
    def replaceMap(self, map: dict):
        mapCopy = {}
        for key, value in map.items():
            if isinstance(value, Variable):
                mapCopy[key] =Variable(nombreSimbolo=value.nombreSimbolo, tipo=value.tipo, ambito=value.ambito, inicializador=value.inicializador)
                 
            elif isinstance(value, Campo):
                newValue =Campo(nombreSimbolo=value.nombreSimbolo, tipo=value.tipo, ambito=value.ambito, inicializador=value.inicializador) 
                newValue.perteneceVariable = value.perteneceVariable
                mapCopy[key] = newValue
            elif isinstance(value, Metodo):
                newValue = Metodo(nombreSimbolo=value.nombreSimbolo, tipo=value.tipo, ambito=value.ambito)
                newValue.contexto = value.contexto
                newValue.parametros = value.parametros
                newValue.variableRetorno = value.variableRetorno
                mapCopy[key] = newValue
            elif isinstance(value, Funcion):
                newValue = Funcion(nombreSimbolo=value.nombreSimbolo, tipo=value.tipo, ambito=value.ambito)
                newValue.contexto = value.contexto
                newValue.parametros = value.parametros
                newValue.variableRetorno = value.variableRetorno
                mapCopy[key] = newValue
            elif isinstance(value, Parametro):
                mapCopy[key] = Parametro(nombreSimbolo=value.nombreSimbolo, tipo=value.tipo, ambito=value.ambito, inicializador=value.inicializador, funcionPertenece=value.perteneceVariable)
            elif isinstance(value, Numero):
                mapCopy[key] = Numero(nombreTipo=value.nombreTipo, valor=value.valor)
            elif isinstance(value, Booleano):
                mapCopy[key] = Booleano(nombreTipo=value.nombreTipo, valor=value.valor)
            elif isinstance(value, Cadena):
                mapCopy[key] = Cadena(nombreTipo=value.nombreTipo, valor=value.valor)
            elif isinstance(value, Nil):
                mapCopy[key] = Nil(nombreTipo=value.nombreTipo, valor=value.valor)
            elif isinstance(value, TipoFuncion):
                newValue = TipoFuncion(nombreTipo=value.nombreTipo, valor=value.valor)
            elif isinstance(value, DefinidoPorUsuario):
                newValue = DefinidoPorUsuario(nombreTipo=value.nombreTipo, valor=value.valor)
                newValue.init = value.init
                newValue.initParams = value.initParams
                newValue.metodosCtx = value.metodosCtx
                newValue.setInheritance(value.inheritance)
                mapCopy[key] = newValue
            elif isinstance(value, Tipo):
                mapCopy[key] = Tipo(nombreTipo=value.nombreTipo, valor=value.valor)
        self.map = mapCopy
    
    def put(self, key, value):
        """Agrega un par clave-valor al HashMap."""
        self.map[key] = value

    def get(self, key):
        """Obtiene el valor asociado a la clave especificada."""
        return self.map.get(key)

    def remove(self, key):
        """Elimina la clave y su valor asociado del HashMap."""
        if key in self.map:
            del self.map[key]

    def contains_key(self, key):
        """Verifica si el HashMap contiene la clave especificada."""
        return key in self.map

    def size(self):
        """Retorna el número de elementos en el HashMap."""
        return len(self.map)

    def is_empty(self):
        """Verifica si el HashMap está vacío."""
        return len(self.map) == 0

    def keys(self):
        """Retorna una lista de todas las claves en el HashMap."""
        return list(self.map.keys())

    def values(self):
        """Retorna una lista de todos los valores en el HashMap."""
        return list(self.map.values())

    def clear(self):
        """Elimina todos los elementos del HashMap."""
        self.map.clear()
    
    def search(self, pattern, search_in_values=False):
        """Busca claves o valores que coincidan con el patrón regex."""
        compiled_pattern = re.compile(pattern)
        if search_in_values:
            return [value for value in self.map.values() if compiled_pattern.match(value)]
        else:
            return [key for key in self.map.keys() if compiled_pattern.match(key)]

class Stack:
    def __init__(self, items=[]):
        self.items = items
    def empty(self):
        return  len(self.items) == 0
    def first(self):
        if len(self.items)>0:
            return  self.items[len(self.items)-1]
        return None
    def remove_first(self):
        if not self.empty():
            return self.items.pop(len(self.items)-1)
        return None
    def insert(self, newElement):
        self.items.append(newElement)
        return self.items
    
class Ambito():
    def __init__(
        self, 
        identificador:int, 
        tablaDeSimbolos:HashMap,
        ) -> None:
        self.identificadorAmbito = identificador
        self.tablaDeSimbolos = tablaDeSimbolos
        # Poner los tipos basicos
        self.tablaDeTipos = HashMap()
        self.tablaDeTipos.replaceMap({"numero": Numero(), "booleano":Booleano(), "cadena": Cadena(), "nil":Nil(), "definidoPorUsuario":DefinidoPorUsuario(), "tipo":Tipo(), "tipoFuncion":TipoFuncion()})
        self.ambitosHijos = set()
    
    # Aniadir contextos hijos
    def aniadirContextoHijo(self, hijo:int):
        self.ambitosHijos.add(hijo)
        
    # Eliminar contextos hijos, por ejemplo, cuando se termina de ejecutar
    def eliminarContextoHijo(self, hijo:int):
        self.ambitosHijos.remove(hijo)