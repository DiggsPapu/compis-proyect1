class Cuadrupleta:
    def __init__(self, operacion=None, arg1=None, arg2=None, resultado=None):
        self.operacion = operacion
        self.arg1 = arg1
        self.arg2 = arg2
        self.resultado = resultado

    def __str__(self):
        # Representación legible del objeto
        if self.operacion is None:
            return f"{self.resultado} = {self.arg1}" if self.arg1 else f"{self.resultado}"
        if self.operacion == 'new_label':
            return f"{self.resultado}:"
        if self.operacion == 'if':
            return f"if {self.arg1} goto {self.resultado}"
        if self.operacion == 'goto':
            return f"goto {self.resultado}"
        return f"{self.resultado} = {self.arg1} {self.operacion} {self.arg2}"

    def __repr__(self):
        # Representación útil para depuración (opcional)
        return self.__str__()
