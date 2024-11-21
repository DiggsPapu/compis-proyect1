class Cuadrupleta:
    def __init__(self, operacion=None, arg1=None, arg2=None, resultado=None):
        self.operacion = operacion
        self.arg1 = arg1
        self.arg2 = arg2
        self.resultado = resultado

    def __str__(self):
        """Definir cómo se imprimirá una Cuadrupleta."""
        return f"{self.resultado} = {self.arg1} {self.operacion} {self.arg2}" if self.arg2 else f"{self.resultado} = {self.operacion} {self.arg1}"

    def __repr__(self):
        """Representación detallada para depuración."""
        return f"Cuadrupleta(operacion={self.operacion}, arg1={self.arg1}, arg2={self.arg2}, resultado={self.resultado})"
