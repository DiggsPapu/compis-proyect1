# Generated from CompiScriptLanguage.g4 by ANTLR 4.13.1
import re
from antlr4 import *

from Semantic.Structures import Ambito, Stack, HashMap, DefinidoPorUsuario, Funcion, Metodo

from .Structures import Cuadrupleta
if "." in __name__:
    from Syntax.CompiScriptLanguageParser import CompiScriptLanguageParser
else:
    from Syntax.CompiScriptLanguageParser import CompiScriptLanguageParser
from antlr4.tree.Tree import TerminalNodeImpl

# This class defines a complete generic visitor for a parse tree produced by CompiScriptLanguageParser.

class CodeGenerator:
    def _init_(self):
        self.label_counter = 0
        self.code = []

    def new_label(self):
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label

    def emit(self, code_line):
        self.code.append(code_line)

    def get_code(self):
        return "\n".join(self.code)

class CompiScriptTacVisitor(ParseTreeVisitor):
    def __init__(self, tablaDeAmbitos, correspondenciaNodosAmbitos, register_manager):
        self.instructions = []  # Lista para almacenar las instrucciones TAC
        self.temp_counter = 0  # Contador para los temporales
        self.param_counter = 0 # Contador para los parametros
        self.tablaDeAmbitos = tablaDeAmbitos    # Tabla de ámbitos con tabla de símbolos y de tipos
        self.correspondenciaNodosAmbitos = correspondenciaNodosAmbitos  # Diccionario que relaciona nodos con ámbitos
        self.ambitoActual = None    # Ámbito actual
        self.label_counter = 0
        self.stackAmbitos = Stack()
        self.intoAmbito = False
        self.code = []
        self.declarandoVariable = None
        self.stackFunciones = Stack([])
        self.tablaDeAmbitos.get(0).aniadirCodigo(Cuadrupleta(operacion='new_label',resultado='main'))
        self.class_name = None
        self.class_herency_name = None
        self.init_method = False
        self.register_manager = register_manager

    def is_string(self, operando):
        """Verifica si un operando es una cadena."""
        # Asegúrate de que operando sea un string y comience/termine con comillas
        return isinstance(operando, str) and (operando.startswith('"') and operando.endswith('"'))

    def searchSomethingInAmbitos(self, something):
        # Primero buscar en el ambito 0 ya que ese es el main y es el final digamos
        retorno = self.tablaDeAmbitos.get(0).tablaDeSimbolos.get(something) if self.tablaDeAmbitos.get(0).tablaDeSimbolos.get(something) else self.tablaDeAmbitos.get(0).tablaDeTipos.get(something)
        if retorno: return retorno
        for i in range(self.tablaDeAmbitos.size()-1,0,-1):
            retorno = self.tablaDeAmbitos.get(i).tablaDeSimbolos.get(something) if self.tablaDeAmbitos.get(i).tablaDeSimbolos.get(something) else self.tablaDeAmbitos.get(i).tablaDeTipos.get(something)
            if retorno: return retorno
        return None
    
    def new_label(self):
        label = f"L{self.label_counter}"
        self.label_counter += 1
        return label

    def emit(self, code_line):
        self.code.append(code_line)

    def get_code(self):
        return "\n".join(self.code)

    def new_temp(self, var_name):
        """Obtener un registro para un temporal."""
        reg = self.register_manager.getReg(var_name)
        return reg

    def free_temp(self, var_name):
        """Liberar un registro asociado a un temporal."""
        self.register_manager.freeReg(var_name)
    
    def generateTAC(self, output_file="compiler/TAC/Tac_output.txt"):
        tac_lines = []
        for instruccion in self.tablaDeAmbitos.get(0).codigo:
            if instruccion.operacion == 'if':
                tac_lines.append(f'    {instruccion.operacion} {instruccion.arg1} {instruccion.resultado}')
            elif instruccion.operacion == None and re.search(r'goto', instruccion.resultado):
                tac_lines.append(f'    {instruccion.resultado}')
            elif instruccion.operacion == 'new_label':
                tac_lines.append(f'{instruccion.resultado}:')
            elif instruccion.operacion == '=':
                tac_lines.append(f'    {instruccion.resultado} = {instruccion.arg1}')
            elif instruccion.operacion == 'EndFunc':
                tac_lines.append(f'    EndFunc')
            elif instruccion.operacion == 'print':
                tac_lines.append(f'    print {instruccion.arg1}')
            elif instruccion.operacion == 'param':
                tac_lines.append(f'    param {instruccion.arg1}')
            elif instruccion.operacion == 'call':
                tac_lines.append(f'    {instruccion.resultado} = call {instruccion.arg1}')
            elif instruccion.operacion == 'pushParam':
                tac_lines.append(f'    pushParam {instruccion.arg1}')
            elif instruccion.operacion == 'popParams':
                tac_lines.append(f'    popParams {instruccion.arg1}')
            elif instruccion.operacion == 'return':
                tac_lines.append(f'    return {instruccion.arg1}')
            elif instruccion.operacion == 'concat':
                tac_lines.append(f'    {instruccion.resultado} = {instruccion.arg1} + {instruccion.arg2}')
            else:
                tac_lines.append(f'    {instruccion.resultado} = {instruccion.arg1} {instruccion.operacion if instruccion.operacion else ""} {instruccion.arg2 if instruccion.arg2 else ""}')

        # Escribir las líneas formateadas en un archivo
        with open(output_file, "w") as f:
            f.write("\n".join(tac_lines))

    def visit(self, ctx):
        """
        This method is called each time a node is visited explicitly.
        """
        self.ultimoAmbito = self.ambitoActual
        if not self.stackFunciones.empty():
            self.ambitoActual = self.stackFunciones.first()
        else: 
            # Asignar el ambito actual
            self.ambitoActual = self.correspondenciaNodosAmbitos.get(ctx)
        # Visit the children of the node (traverse the tree)
        return super().visit(ctx)

    def visitChildren(self, ctx):
        """
        This method is called each time a node's children are visited.
        """
        self.ultimoAmbito = self.ambitoActual
        if not self.stackFunciones.empty():
            self.ambitoActual = self.stackFunciones.first()
        else: 
            # Asignar el ambito actual
            self.ambitoActual = self.correspondenciaNodosAmbitos.get(ctx)
        # Continue visiting the children as usual
        return super().visitChildren(ctx)
    
    # Método para manejar una operacion basica
    def handleBasicOperation(self, ctx):
        def procesar_operadores(operadores, operandos):
            # Procesar operadores con mayor precedencia (*, /)
            while len(operadores) > 0:
                operador = operadores.pop(0)
                operando1 = operandos.pop(0)
                operando2 = operandos.pop(0)
                
                # Verificar si es concatenación de cadenas
                if operador == '+' and (self.is_string(operando1) or self.is_string(operando2)):
                    instruction = Cuadrupleta()
                    instruction.arg1 = operando1
                    instruction.operacion = 'concat'  # Nuevo tipo de operación para concatenación
                    instruction.arg2 = operando2
                    instruction.resultado = self.new_temp("temp_concat")
                    self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(instruction)

                    operandos.insert(0, instruction.resultado)  # Guardar el resultado como operando
                else:
                    instruction = Cuadrupleta()
                    instruction.arg1 = operando1
                    instruction.operacion = operador
                    instruction.arg2 = operando2
                    instruction.resultado = self.new_temp("temp_result")
                    self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(instruction)

                    operandos.insert(0, instruction.resultado)

                # Liberar registros temporales usados
                self.free_temp(operando1)
                self.free_temp(operando2)

        # Si solo hay un término (número o variable)
        if ctx.getChildCount() == 1:
            return self.visit(ctx.getChild(0))

        # Separar operadores y operandos
        operandos = []
        operadores = []
        
        for i in range(ctx.getChildCount()):
            if i % 2 == 0:  # Es un operando
                operandos.append(self.visit(ctx.getChild(i)))
            else:  # Es un operador
                operadores.append(ctx.getChild(i).getText())
        
        # Primero, procesar operadores de mayor precedencia (*, /)
        operadores_pendientes = []
        operandos_pendientes = [operandos.pop(0)]  # El primer operando

        i = 0
        while i < len(operadores):
            operador = operadores[i]
            if operador in ['*', '/', '%', 'and', '>', '>=', '<', '<=', '!=', '==']:
                instruction = Cuadrupleta()
                instruction.arg1 = operandos_pendientes.pop()  # Último operando procesado
                instruction.operacion = operador
                instruction.arg2 = operandos.pop(0)  # Siguiente operando
                
                instruction.resultado = self.new_temp("temp_high_precedence")
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(instruction)
                
                operandos_pendientes.append(instruction.resultado)  # Guardar el resultado

                # Liberar registros temporales usados
                self.free_temp(instruction.arg1)
                self.free_temp(instruction.arg2)
            else:
                operadores_pendientes.append(operador)
                operandos_pendientes.append(operandos.pop(0))  # Guardar el siguiente operando pendiente
            i += 1

        # Luego, procesar operadores de menor precedencia (+, -)
        procesar_operadores(operadores_pendientes, operandos_pendientes)
        
        # El último resultado es el valor final
        return operandos_pendientes[0]
         
    # Visit a parse tree produced by CompiScriptLanguageParser#program.
    def visitProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        # Recorrer el programa
        for child in ctx.declaration():
            self.visit(child)


    # Visit a parse tree produced by CompiScriptLanguageParser#declaration.
    def visitDeclaration(self, ctx:CompiScriptLanguageParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#classDecl.
    def visitClassDecl(self, ctx:CompiScriptLanguageParser.ClassDeclContext):
        self.class_name = ctx.IDENTIFIER(0).getText()
        # herencia
        if ctx.IDENTIFIER(1):
            self.class_herency_name = ctx.IDENTIFIER(1).getText()
            claseHerencia:DefinidoPorUsuario = self.searchSomethingInAmbitos(f'{self.class_herency_name}')
            claseHeredar:DefinidoPorUsuario = self.searchSomethingInAmbitos(f'{self.class_name}')
            for index in range(len(claseHerencia.atributos)-1, -1, -1):
                claseHeredar.atributos.insert(0, claseHerencia.atributos[index])
        # Practicamente crear una clase es hacer todos sus metodos
        for child in ctx.function():
            self.visit(child)
        self.class_name = None
        self.class_herency_name = None


    # Visit a parse tree produced by CompiScriptLanguageParser#funDecl.
    def visitFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        return self.visit(ctx.function())


    # Visit a parse tree produced by CompiScriptLanguageParser#varDecl.
    def visitVarDecl(self, ctx: CompiScriptLanguageParser.VarDeclContext):
        instruccion = Cuadrupleta()
        instruccion.resultado = ctx.IDENTIFIER().getText()  # Nombre de la variable
        self.declarandoVariable = instruccion.resultado

        # Asignar directamente si hay una expresión, de lo contrario, omitir
        if ctx.expression():
            instruccion.arg1 = self.visit(ctx.expression())
            instruccion.operacion = "="
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(instruccion)

        self.declarandoVariable = None
        return instruccion.resultado

    # Visit a parse tree produced by CompiScriptLanguageParser#statement.
    def visitStatement(self, ctx:CompiScriptLanguageParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#exprStmt.
    def visitExprStmt(self, ctx:CompiScriptLanguageParser.ExprStmtContext):
        return self.visit(ctx.expression())


    # Visit a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def visitIfStmt(self, ctx:CompiScriptLanguageParser.IfStmtContext):
        ambitoIf = self.ambitoActual
        rangoBlock = len(ctx.block())
        rangoExpr = len(ctx.expression())
        ifInstr = []
        blockInstr = []
        # Crear el label para el despues
        labelDespues = Cuadrupleta(operacion='new_label',resultado=self.new_label())
        gotoDespues = Cuadrupleta(resultado = f'goto {labelDespues.resultado}')
        
        for index in range(rangoBlock-1,-1,-1):
            instruccion = Cuadrupleta()
            instruccionLabel = Cuadrupleta(operacion='new_label', resultado=self.new_label())
            blockInstr.append(instruccionLabel)
            if not self.stackFunciones.empty():
                numAmbito = self.tablaDeAmbitos.size()
                # crear un ambito para el if entonces y que se desarrolle ahi
                AmbitoIf = Ambito(numAmbito, HashMap())
                self.tablaDeAmbitos.put(numAmbito, AmbitoIf)
                self.ambitoActual = numAmbito
                self.stackFunciones.insert(numAmbito)
            # Generar el codigo del bloque de primero
            self.visit(ctx.block(index))
            # Aniadir el bloque de codigo al ambito actual
            blockInstr.extend(self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).codigo)
            blockInstr.append(gotoDespues)
            self.ultimoAmbito = self.ambitoActual
            self.ambitoActual = ambitoIf
            if not self.stackFunciones.empty(): 
                self.stackFunciones.remove_first()
            # Significa que hay un else
            if rangoBlock>rangoExpr and index==rangoBlock-1:
                instruccion.resultado = f'goto {instruccionLabel.resultado}'
            else:
                instruccion.operacion = 'if'
                instruccion.resultado = f'goto {instruccionLabel.resultado}'
                instruccion.arg1 = self.visit(ctx.expression(index))
            ifInstr.append(instruccion)
        ifInstr.reverse()
        for instruccion in ifInstr: 
            self.tablaDeAmbitos.get(ambitoIf).aniadirCodigo(instruccion)
        self.tablaDeAmbitos.get(ambitoIf).aniadirCodigo(gotoDespues)
        for instruccion in blockInstr:
            self.tablaDeAmbitos.get(ambitoIf).aniadirCodigo(instruccion)
        self.tablaDeAmbitos.get(ambitoIf).aniadirCodigo(labelDespues)


    # Visit a parse tree produced by CompiScriptLanguageParser#forStmt.
    def visitForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        ambitoFor = self.ambitoActual
        # la declaracion de variable debe de estar en el flujo normal por ende no estara dentro del label, igual si se reasigna el valor de una variable
        # Crear temporal para la variable que se va a reasignar
        variable = None
        if ctx.varDecl():
            variable = self.visit(ctx.varDecl())
        elif ctx.exprStmt():
            variable = self.visit(ctx.exprStmt())
        # Crear un nuevo label para evaluar la condicion del for
        checkLabel = Cuadrupleta(operacion = 'new_label',resultado = self.new_label())
        self.tablaDeAmbitos.get(ambitoFor).aniadirCodigo(checkLabel)
        # Crear un nuevo label para evaluar el bloque del for
        blockLabel = Cuadrupleta(operacion='new_label',resultado=self.new_label())
        # Crear un nuevo label para la continuacion luego del for
        continueLabel = Cuadrupleta(operacion='new_label',resultado=self.new_label())
        # La primera expresion suele ser la de la condicion
        if ctx.expression():
            instruccion = Cuadrupleta(operacion='if',arg1=self.visit(ctx.expression(0)),resultado=f'goto {blockLabel.resultado}')
            self.tablaDeAmbitos.get(ambitoFor).aniadirCodigo(instruccion)
        # Crear goto a la continuacion en caso de que no aplique
        instruccion = Cuadrupleta(resultado=f'goto {continueLabel.resultado}')
        self.tablaDeAmbitos.get(ambitoFor).aniadirCodigo(instruccion)
        # Aniadir el label del bloque para que lo demas sea parte del bloque
        self.tablaDeAmbitos.get(ambitoFor).aniadirCodigo(blockLabel)
        if not self.stackFunciones.empty():
            numAmbito = self.tablaDeAmbitos.size()
            # crear un ambito para el if entonces y que se desarrolle ahi
            AmbitoIf = Ambito(numAmbito, HashMap())
            self.tablaDeAmbitos.put(numAmbito, AmbitoIf)
            self.ambitoActual = numAmbito
            self.stackFunciones.insert(numAmbito)
        # Generar el bloque de codigo del for
        self.visit(ctx.block())
        if not self.stackFunciones.empty():
            self.stackFunciones.remove_first()
        self.tablaDeAmbitos.get(ambitoFor).aniadirCodigoCompleto(self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).codigo, self.tablaDeAmbitos.get(ambitoFor).codigo_pointer.first())
        # Condicion de sumar o lo que sea de la segunda expresion, eso va adentro del bloque
        if len(ctx.expression())>1:
            sumaOLoQueSea = Cuadrupleta(operacion='=',arg1=self.visit(ctx.expression(1)),resultado=variable)
            self.tablaDeAmbitos.get(ambitoFor).aniadirCodigo(sumaOLoQueSea)
        # Agregar el goto para el bloque del for para que evalue la condicion
        instruccion = Cuadrupleta(resultado=f'goto {checkLabel.resultado}')
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(instruccion)
        # Aniadir el label de la continuacion
        self.tablaDeAmbitos.get(ambitoFor).aniadirCodigo(continueLabel)

    # Visit a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def visitWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        ambitoWhile = self.ambitoActual
        # Crear un nuevo label para evaluar la condicion del while
        checkLabel = self.new_label()
        # Crear un nuevo label para la continuacion
        continueLabel = self.new_label()
        # Crear una instruccion en el flujo para que lleve al nuevo label en cuestión
        instruccion = Cuadrupleta()
        instruccion.resultado = f'goto {checkLabel}'
        self.tablaDeAmbitos.get(ambitoWhile).aniadirCodigo(instruccion)
        # Crear una instruccion que sea un nuevo label
        instruccion = Cuadrupleta()
        instruccion.operacion = 'new_label'
        instruccion.resultado = checkLabel
        self.tablaDeAmbitos.get(ambitoWhile).aniadirCodigo(instruccion)
        # Crear una instruccion que sea un if
        instruccion = Cuadrupleta()
        instruccion.operacion = 'if'
        instruccion.arg1 = self.visit(ctx.expression())
        if not self.stackFunciones.empty():
            numAmbito = self.tablaDeAmbitos.size()
            # crear un ambito para el if entonces y que se desarrolle ahi
            AmbitoIf = Ambito(numAmbito, HashMap())
            self.tablaDeAmbitos.put(numAmbito, AmbitoIf)
            self.ambitoActual = numAmbito
            self.stackFunciones.insert(numAmbito)
        # Crear un nuevo label para el bloque del while
        blockLabel = Cuadrupleta()
        blockLabel.resultado = self.new_label()
        blockLabel.operacion = 'new_label'
        self.visit(ctx.block())
        self.ultimoAmbito = self.ambitoActual
        self.ambitoActual = ambitoWhile
        # Irse al bloque del while
        instruccion.resultado = f'goto {blockLabel.resultado}'
        self.tablaDeAmbitos.get(ambitoWhile).aniadirCodigo(instruccion)
        # Irse a la continuacion
        instruccionContinue = Cuadrupleta(resultado=f'goto {continueLabel}')
        self.tablaDeAmbitos.get(ambitoWhile).aniadirCodigo(instruccionContinue)
        # Aniadir el goto al bloque del while
        instruccion = Cuadrupleta()
        instruccion.resultado = f'goto {checkLabel}'
        self.tablaDeAmbitos.get(self.ultimoAmbito).aniadirCodigo(instruccion)
        # Aniadir el bloque del while al ambito actual
        self.tablaDeAmbitos.get(ambitoWhile).aniadirCodigo(blockLabel)
        for instruccion in self.tablaDeAmbitos.get(self.ultimoAmbito).codigo:
            self.tablaDeAmbitos.get(ambitoWhile).aniadirCodigo(instruccion)
        # Crear una instruccion que sea un nuevo label
        instruccion = Cuadrupleta(resultado=continueLabel,operacion='new_label')
        self.tablaDeAmbitos.get(ambitoWhile).aniadirCodigo(instruccion)
        if not self.stackFunciones.empty():
            self.stackFunciones.remove_first()

    # Visit a parse tree produced by CompiScriptLanguageParser#printStmt.
    def visitPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(Cuadrupleta(arg1=self.visit(ctx.expression()),operacion='print'))
        return 'null'


    # Visit a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def visitReturnStmt(self, ctx:CompiScriptLanguageParser.ReturnStmtContext):
        retorno = Cuadrupleta(operacion='return', arg1=self.visit(ctx.expression()) if ctx.expression() else 'null')
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(retorno)
        return retorno.arg1


    # Visit a parse tree produced by CompiScriptLanguageParser#block.
    def visitBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#expression.
    def visitExpression(self, ctx: CompiScriptLanguageParser.ExpressionContext):
        if ctx.array():
            return self.visit(ctx.array())
        elif ctx.logic():
            return self.visit(ctx.logic())
        else:
            # Es una asignación simple
            if ctx.getChildCount() == 3 and ctx.getChild(1).getText() == "=":
                variable = ctx.getChild(0).getText()
                valor = self.visit(ctx.getChild(2))

                # Crear instrucción de asignación
                asignacion = Cuadrupleta(
                    operacion="=",
                    arg1=valor,
                    resultado=variable
                )
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(asignacion)
                return variable

            # Caso de operación aritmética
            return self.handleBasicOperation(ctx)

    # Visit a parse tree produced by CompiScriptLanguageParser#array.
    def visitArray(self, ctx:CompiScriptLanguageParser.ArrayContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arrayCreation.
    def visitArrayCreation(self, ctx: CompiScriptLanguageParser.ArrayCreationContext):
        instruccion = Cuadrupleta()

        # Es un array de arrays o con elementos primitivos
        if ctx.logic() or ctx.array():
            direccionesDeMemoria = []
            inicial = None
            for index in range(len(ctx.logic() if ctx.logic() else ctx.array())):
                # Temporal para el valor
                valor_temp = self.new_temp(f"valor_temp_{index}")
                valor = Cuadrupleta(
                    arg1=self.visit(ctx.logic(index) if ctx.logic() else ctx.array(index)),
                    operacion='=',
                    resultado=valor_temp
                )
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(valor)

                # Dirección de memoria
                direccion_temp = self.new_temp(f"direccion_temp_{index}")
                direccion = Cuadrupleta(arg1=f'&{valor.resultado}', operacion='=', resultado=direccion_temp)
                if inicial is None:
                    inicial = direccion.resultado
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(direccion)
                direccionesDeMemoria.append(direccion.resultado)

                # Liberar temporales usados
                self.free_temp(valor_temp)

            for index in range(0, len(direccionesDeMemoria), 2):
                direccion1 = direccionesDeMemoria[index]
                direccion2 = direccionesDeMemoria[index + 1] if index + 1 < len(direccionesDeMemoria) else 'null'

                # Temporal para calcular la dirección de memoria del puntero
                puntero_temp = self.new_temp(f"puntero_temp_{index}")
                punteroDireccion = Cuadrupleta(arg1=direccion1, operacion='+', arg2=16, resultado=puntero_temp)  # 16 bytes
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(punteroDireccion)

                # Asignar la dirección de memoria al puntero
                asignarMemoria = Cuadrupleta(arg1=direccion2, operacion='=', resultado=f'*{punteroDireccion.resultado}')
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(asignarMemoria)

                if index == len(direccionesDeMemoria) - 2:
                    ultimoPuntero_temp = self.new_temp("ultimo_puntero_temp")
                    ultimoPuntero = Cuadrupleta(arg1=direccion2, operacion='+', arg2=16, resultado=ultimoPuntero_temp)
                    self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(ultimoPuntero)
                    self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(
                        Cuadrupleta(arg1='null', operacion='=', resultado=f'*{ultimoPuntero.resultado}')
                    )

                    # Liberar el último puntero
                    self.free_temp(ultimoPuntero_temp)

                # Liberar puntero temporal
                self.free_temp(puntero_temp)

            return inicial

        # Es un array vacío
        else:
            # Temporal para inicializar el array vacío
            array_temp = self.new_temp("array_vacio_temp")
            instruccion = Cuadrupleta(arg1='null', operacion='=', resultado=array_temp)
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(instruccion)

            # Calcular la dirección de memoria del puntero
            puntero_temp = self.new_temp("puntero_direccion_temp")
            punteroDireccion = Cuadrupleta(arg1=f'&{instruccion.resultado}', operacion='+', arg2=16, resultado=puntero_temp)
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(punteroDireccion)

            # Asignar memoria al puntero
            asignarMemoria = Cuadrupleta(arg1='null', operacion='=', resultado=f'*{punteroDireccion.resultado}')
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(asignarMemoria)

            # Liberar temporales
            self.free_temp(array_temp)
            self.free_temp(puntero_temp)

            return f'&{instruccion.resultado}'

    # Visit a parse tree produced by CompiScriptLanguageParser#arrayAccess.
    def visitArrayAccess(self, ctx: CompiScriptLanguageParser.ArrayAccessContext):
        retorno = None
        
        # Obtener un registro temporal para el array
        array = self.new_temp("array_temp")
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(
            Cuadrupleta(arg1=ctx.IDENTIFIER().getText(), operacion='=', resultado=array)
        )

        for index in range(len(ctx.NUMBER())):
            # Cargar el índice que se busca 
            number = ctx.NUMBER(index).getText()
            indiceBuscado = Cuadrupleta(arg1=number, operacion='=', resultado=self.new_temp("indice_temp"))
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(indiceBuscado)

            # Crear un índice inicial de 0
            indice = Cuadrupleta(arg1=0, operacion='=', resultado=self.new_temp("indice_inicial_temp"))
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(indice)

            # Crear un label
            checkLabel = self.new_label()
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(
                Cuadrupleta(operacion='new_label', resultado=checkLabel)
            )

            # Calcular la dirección de memoria del puntero
            punteroDireccion = Cuadrupleta(arg1=array, operacion='+', arg2=16, resultado=self.new_temp("puntero_temp"))
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(punteroDireccion)

            # Verificar si ya se llegó al puntero nulo (último)
            ultimoPuntero = Cuadrupleta(
                arg1=indiceBuscado.resultado, operacion='!=', arg2=indice.resultado, resultado=self.new_temp("ultimo_temp")
            )
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(ultimoPuntero)

            # Sumar uno al índice
            indice = Cuadrupleta(arg1=1, operacion='+', arg2=indice.resultado, resultado=indice.resultado)
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(indice)

            # Crear una instrucción `if` para verificar si se llegó al puntero nulo
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(
                Cuadrupleta(operacion='if', arg1=ultimoPuntero.resultado, resultado=f'goto {checkLabel}')
            )

            # Almacenar el valor encontrado en un registro temporal
            retorno = Cuadrupleta(arg1=f'*{punteroDireccion.resultado}', operacion='=', resultado=self.new_temp("valor_temp"))
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(retorno)

            # Liberar registros temporales que ya no se necesitan
            self.free_temp("indice_temp")
            self.free_temp("indice_inicial_temp")
            self.free_temp("puntero_temp")
            self.free_temp("ultimo_temp")

        # Liberar el registro del array
        self.free_temp("array_temp")

        return retorno.resultado

    # Visit a parse tree produced by CompiScriptLanguageParser#arrayPush.
    def visitArrayPush(self, ctx:CompiScriptLanguageParser.ArrayPushContext):
        if ctx.array() or ctx.logic():
            array = self.new_temp()
            # Obtener el nombre del array de la variable
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(Cuadrupleta(arg1=ctx.IDENTIFIER().getText(), operacion='=', resultado=array))
            # Obtener el valor que se va a pushear
            elementoTemporal = Cuadrupleta(arg1=self.visit(ctx.logic() if ctx.logic() else ctx.array()), operacion='=', resultado=self.new_temp())
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(elementoTemporal)
            # No permito array de nulos entonces si tiene un nulo en la posicion se le asigna el valor, ya que esto significa que es la primera posicion
            comparacion = Cuadrupleta(arg1=f'*{array}',operacion='==',arg2='null',resultado=self.new_temp())
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(comparacion)
            # Crear label para guardar la variable y asignar el ultimo puntero a null
            labelSave = self.new_label()
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(Cuadrupleta(operacion='if',arg1=comparacion.resultado,resultado=f'goto {labelSave}'))            
            # Moverse dentro de la direccion de memoria del puntero
            # Crear label
            checkLabel = self.new_label()
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(Cuadrupleta(operacion='new_label',resultado=checkLabel))
            # Crear temporal para calcular la direccion de memoria que tendra el puntero
            punteroDireccion = Cuadrupleta(arg1=array,operacion='+',arg2=16,resultado=array)
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(punteroDireccion)
            # Crear temporal para verificar si ya se llego al puntero nulo que es el ultimo
            ultimoPuntero = Cuadrupleta(arg1=f'*{punteroDireccion.resultado}',operacion='!=',arg2='null',resultado=self.new_temp())
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(ultimoPuntero)
            # Crear if para verificar si ya se llego al puntero nulo que es el ultimo
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(Cuadrupleta(operacion='if',arg1=ultimoPuntero.resultado,resultado=f'goto {checkLabel}'))
            # Label para guardar la variable y asignar el ultimo puntero a null
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(Cuadrupleta(operacion='new_label',resultado=labelSave))
            # Crear la instruccion para asignar el valor al puntero
            asignarMemoria = Cuadrupleta(arg1=f'&{elementoTemporal.resultado}',operacion='=',resultado=f'*{punteroDireccion.resultado}')
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(asignarMemoria)
            # Crear la instruccion para calcular la direccion de memoria que tendra el puntero nulo que es el ultimo
            punteroDireccion = Cuadrupleta(arg1=f'&{punteroDireccion.resultado}',operacion='+',arg2=16,resultado=self.new_temp())
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(punteroDireccion)
            # Crear la instruccion para asignar el puntero al siguiente puntero que es nulo
            siguientePuntero = Cuadrupleta(arg1='null',operacion='=',resultado=f'*{punteroDireccion.resultado}')
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(siguientePuntero)
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arrayPop.
    def visitArrayPop(self, ctx:CompiScriptLanguageParser.ArrayPopContext):
        array = self.new_temp()
        # Obtener el nombre del array de la variable
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(Cuadrupleta(arg1=ctx.IDENTIFIER().getText(), operacion='=', resultado=array))  
        # Get the last element of the array
        # Crear label
        checkLabel = self.new_label()
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(Cuadrupleta(operacion='new_label',resultado=checkLabel))
        # Crear temporal para el valor actual de la direccion de memoria ya que en caso se encuentre este sera el que tendra que ser null
        punteroPosibleNull = Cuadrupleta(arg1=array,operacion='=',resultado=self.new_temp())
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(punteroPosibleNull)
        # Crear temporal para calcular la direccion de memoria que tendra el puntero
        punteroDireccion = Cuadrupleta(arg1=array,operacion='+',arg2=16,resultado=array)
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(punteroDireccion)
        # Crear temporal para verificar si ya se llego al puntero nulo que es el ultimo
        ultimoPuntero = Cuadrupleta(arg1=f'*{punteroDireccion.resultado}',operacion='!=',arg2='null',resultado=self.new_temp())
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(ultimoPuntero)
        # Crear if para verificar si ya se llego al puntero nulo que es el ultimo
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(Cuadrupleta(operacion='if',arg1=ultimoPuntero.resultado,resultado=f'goto {checkLabel}'))
        # Variable temporal para retornar el valor del puntero
        retorno = Cuadrupleta(arg1=f'*{punteroPosibleNull.resultado}',operacion='=',resultado=self.new_temp())
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(retorno)
        # Setear el puntero a null
        self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(Cuadrupleta(arg1='null',operacion='=',resultado=f'{punteroPosibleNull.resultado}'))
        return retorno.resultado
        

    # Visit a parse tree produced by CompiScriptLanguageParser#logic.
    def visitLogic(self, ctx:CompiScriptLanguageParser.LogicContext):
        return self.handleBasicOperation(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#comparison.
    def visitComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        return self.handleBasicOperation(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#term.
    def visitTerm(self, ctx: CompiScriptLanguageParser.TermContext):
        return self.handleBasicOperation(ctx)

    # Visit a parse tree produced by CompiScriptLanguageParser#unary.
    def visitUnary(self, ctx: CompiScriptLanguageParser.UnaryContext):
        # En caso de que sea una call que retorne solo el call
        if ctx.call():
            return self.visit(ctx.call())

        # Esto implica que puede negarse el valor o puede volverse negativo
        if ctx.unary():
            instruction = Cuadrupleta()
            
            # Obtener un registro temporal para el resultado de la operación unaria
            temporal_resultado = self.new_temp("unary_temp")
            instruction.resultado = temporal_resultado
            instruction.operacion = ctx.getChild(0).getText()
            instruction.arg1 = ''
            
            # Obtener el registro temporal del operando
            operando = self.visit(ctx.unary())
            instruction.arg2 = operando
            
            # Añadir la instrucción al ámbito actual
            self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual is not None else 0).aniadirCodigo(instruction)

            # Liberar el registro temporal del operando
            self.free_temp(operando)
            
            return temporal_resultado

    # Visit a parse tree produced by CompiScriptLanguageParser#call.
    def visitCall(self, ctx: CompiScriptLanguageParser.CallContext):
        # Solo es un primary
        if ctx.getChildCount() == 1:
            return self.visit(ctx.primary())

        # En caso de que no solo sea un primary
        # Es crear una clase
        elif isinstance(ctx.getChild(0), TerminalNodeImpl) and ctx.getChild(0).getText() == "new":
            ambitoLlamada = self.ambitoActual
            class_name = self.visit(ctx.primary())
            temporalParaAlmacenarObjeto = self.new_temp("temp_objeto")
            objetoInstr = Cuadrupleta(operacion='pushParam', arg1=temporalParaAlmacenarObjeto)
            self.tablaDeAmbitos.get(ambitoLlamada).aniadirCodigo(objetoInstr)

            parametros = self.visit(ctx.arguments(0)) if ctx.arguments() else []
            for parametro in parametros:
                parametroInstr = Cuadrupleta(operacion='pushParam', arg1=parametro)
                self.tablaDeAmbitos.get(ambitoLlamada).aniadirCodigo(parametroInstr)

            # Crear una instrucción para el call y el retorno
            temporalRetorno = self.new_temp("temp_retorno")
            callInstr = Cuadrupleta(resultado=temporalRetorno, operacion='call', arg1=f'{class_name}_init')
            self.tablaDeAmbitos.get(ambitoLlamada).aniadirCodigo(callInstr)

            # pop params
            popParams = Cuadrupleta(operacion='popParams', arg1=len(parametros))
            self.tablaDeAmbitos.get(ambitoLlamada).aniadirCodigo(popParams)

            self.free_temp("temp_objeto")
            self.free_temp("temp_retorno")
            return temporalParaAlmacenarObjeto

        # Es una llamada a una función o a una clase y atributos o una clase y métodos
        else:
            firstPrimary = self.visit(ctx.primary())
            value = self.searchSomethingInAmbitos(firstPrimary)
            stackFuncionesWasEmpty = self.stackFunciones.empty()

            if stackFuncionesWasEmpty:
                self.stackFunciones.insert(self.ambitoActual)

            # Clase o función
            if isinstance(value, Funcion):
                parametros = self.visit(ctx.arguments(0)) if ctx.arguments() else []
                for parametro in parametros:
                    parametroInstr = Cuadrupleta(operacion='pushParam', arg1=parametro)
                    self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual else 0).aniadirCodigo(parametroInstr)

                temporalRetorno = self.new_temp("temp_retorno")
                callInstr = Cuadrupleta(resultado=temporalRetorno, operacion='call', arg1=firstPrimary)
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual else 0).aniadirCodigo(callInstr)

                popParams = Cuadrupleta(operacion='popParams', arg1=len(value.parametros))
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual else 0).aniadirCodigo(popParams)

                self.free_temp("temp_retorno")

            if stackFuncionesWasEmpty:
                self.stackFunciones.remove_first()

            if firstPrimary == 'this' and self.class_name:
                for index in range(1, ctx.getChildCount()):
                    node = ctx.getChild(index)
                    if isinstance(node, TerminalNodeImpl):
                        child = ctx.getChild(index).getText()
                        value = self.searchSomethingInAmbitos(f'{self.class_name}.{child}')
                        if child == '.':
                            continue

                        elif value:
                            if isinstance(value, Funcion):
                                parametros = []
                                while ctx.getChild(index).getText() != ')':
                                    if not isinstance(ctx.getChild(index), TerminalNodeImpl):
                                        possibleParameter = self.visit(ctx.getChild(index))
                                        parametros.append(possibleParameter)
                                    index += 1

                                for parametro in parametros:
                                    parametroInstr = Cuadrupleta(operacion='pushParam', arg1=parametro)
                                    self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual else 0).aniadirCodigo(parametroInstr)

                                temporalRetorno = self.new_temp("temp_retorno")
                                callInstr = Cuadrupleta(resultado=temporalRetorno, operacion='call', arg1=f'{self.class_name}.{child}')
                                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual else 0).aniadirCodigo(callInstr)

                                popParams = Cuadrupleta(operacion='popParams', arg1=len(value.parametros))
                                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual else 0).aniadirCodigo(popParams)

                                self.free_temp("temp_retorno")
                        else:
                            # Manejo de atributos
                            listaAtributos = self.searchSomethingInAmbitos(f'{self.class_name}').atributos
                            if child in listaAtributos:
                                offset = listaAtributos.index(child) * 16  # Offset asumido de 16 bytes por atributo
                                direccionAtributo = Cuadrupleta(
                                    operacion='+',
                                    arg1='object',  # `object` es el puntero a la instancia actual
                                    arg2=str(offset),
                                    resultado=self.new_temp("temp_direccion")
                                )
                                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual else 0).aniadirCodigo(direccionAtributo)

                                # Retornar la dirección calculada
                                return direccionAtributo.resultado
                            else:
                                raise Exception(f"El atributo '{child}' no existe en la clase '{self.class_name}'.")

            return firstPrimary

    # Visit a parse tree produced by CompiScriptLanguageParser#primary.
    def visitPrimary(self, ctx: CompiScriptLanguageParser.PrimaryContext):
        if ctx.IDENTIFIER():
            identifier = ctx.IDENTIFIER().getText()
            # Si estamos dentro de una clase y el identificador pertenece a un atributo
            if self.class_name and identifier in self.searchSomethingInAmbitos(f'{self.class_name}').atributos:
                listaAtributos = self.searchSomethingInAmbitos(f'{self.class_name}').atributos
                offset = listaAtributos.index(identifier) * 16  # Offset basado en el índice del atributo
                temp_direccion = self.new_temp("temp_direccion")
                direccionAtributo = Cuadrupleta(
                    operacion='+',
                    arg1='object',  # El puntero a la instancia actual
                    arg2=str(offset),
                    resultado=temp_direccion
                )
                self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual else 0).aniadirCodigo(direccionAtributo)
                return f'*{temp_direccion}'
            else:
                # Si no es un atributo, retornar el identificador como está
                return identifier

        elif ctx.NUMBER():
            return ctx.NUMBER().getText()

        elif ctx.STRING():
            return ctx.STRING().getText()

        elif ctx.expression():
            return self.visit(ctx.expression())

        # Array access
        elif ctx.arrayAccess():
            return self.visit(ctx.arrayAccess())

        elif ctx.getText() == "nil":
            return "null"

        elif ctx.getText() in ["false", "true", "this"]:
            if ctx.getText() == "this" and self.class_name:
                return "object"  # `object` representa el puntero a la instancia actual
            return ctx.getText()

        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#function.
    def visitFunction(self, ctx: CompiScriptLanguageParser.FunctionContext):
        # Crear un nuevo ámbito
        numAmbito = self.tablaDeAmbitos.size()
        newFunctionAmbito = Ambito(identificador=numAmbito, tablaDeSimbolos=HashMap())
        self.stackFunciones.insert(numAmbito)
        self.tablaDeAmbitos.put(numAmbito, newFunctionAmbito)

        # Crear una instrucción para el label de la función
        nombreFuncion = ctx.IDENTIFIER().getText()
        instruccion = Cuadrupleta(
            operacion='new_label',
            resultado=nombreFuncion if not self.class_name else f'{self.class_name}_{nombreFuncion}'
        )
        self.tablaDeAmbitos.get(numAmbito).aniadirCodigo(instruccion)

        # Manejo de herencia
        if nombreFuncion == 'init' and self.class_herency_name is not None:
            funcionInitHerencia: Metodo = self.searchSomethingInAmbitos(f'{self.class_herency_name}.init')
            if funcionInitHerencia:
                for parametro in funcionInitHerencia.parametros:
                    parametroInstr = Cuadrupleta(operacion='pushParam', arg1=parametro)
                    self.tablaDeAmbitos.get(numAmbito).aniadirCodigo(parametroInstr)

                # Crear un temporal para la llamada al método heredado
                temp_call = self.new_temp("call_init_herencia_temp")
                callInstr = Cuadrupleta(
                    operacion='call',
                    arg1=f'{self.class_herency_name}_init',
                    resultado=temp_call
                )
                self.tablaDeAmbitos.get(numAmbito).aniadirCodigo(callInstr)

                # Crear instrucción para popParams
                popInstr = Cuadrupleta(
                    operacion='popParams',
                    arg1=len(funcionInitHerencia.parametros)
                )
                self.tablaDeAmbitos.get(numAmbito).aniadirCodigo(popInstr)

                # Liberar el registro temporal utilizado para la llamada
                self.free_temp(temp_call)

        if self.class_name:
            nombreFuncion = f'{self.class_name}.{nombreFuncion}'
            # Añadir parámetro de objeto
            self.tablaDeAmbitos.get(numAmbito).aniadirCodigo(
                Cuadrupleta(operacion='param', arg1='object')
            )

        # Manejo de parámetros de la función
        simboloFuncion: Funcion = self.searchSomethingInAmbitos(nombreFuncion)
        for parametro in simboloFuncion.parametros:
            parametroInstruccion = Cuadrupleta(operacion='param', arg1=parametro)
            self.tablaDeAmbitos.get(numAmbito).aniadirCodigo(parametroInstruccion)

        # Generar el código del bloque de la función
        self.visit(ctx.block())

        # Añadir endFunc
        endFunc = Cuadrupleta(operacion='EndFunc')
        self.tablaDeAmbitos.get(numAmbito).aniadirCodigo(endFunc)

        # Actualizar los ámbitos
        self.stackFunciones.remove_first()
        self.tablaDeAmbitos.get(0).aniadirCodigoCompleto(
            self.tablaDeAmbitos.get(numAmbito).codigo, 0
        )

    # Visit a parse tree produced by CompiScriptLanguageParser#parameters.
    def visitParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arguments.
    def visitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        parametros = []
        for child in ctx.expression():
            parametros.append(self.visit(child))
        return parametros
        # Appendear los argumentos en el tac 
        # for child in ctx.expression():
        #     parametro = self.visit(child)
        #     instruccion = Cuadrupleta(operacion='param',arg1=parametro)
        #     self.tablaDeAmbitos.get(self.ambitoActual if self.ambitoActual != None else 0).aniadirCodigo(instruccion)