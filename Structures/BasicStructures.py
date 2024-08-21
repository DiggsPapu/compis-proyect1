import copy
import re
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
        self.map = map 
    
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
        return  self.items[len(self.items)-1]
    def remove_first(self):
        if not self.empty():
            return self.items.pop(len(self.items)-1)
        return None
    def insert(self, newElement):
        self.items.append(newElement)
        return self.items