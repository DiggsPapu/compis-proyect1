from Syntax.CompiScriptLanguageVisitor import *
from Syntax.CompiScriptLanguageParser import *
from .Structures import HashMap, Ambito, Variable, Numero, Nil, Simbolo, Tipo, TipoFuncion, Funcion, Booleano, DefinidoPorUsuario, Stack, Campo, Parametro, Cadena, Metodo
from antlr4.tree.Tree import TerminalNodeImpl
import re
# Manejo de errores lexicos
class LexicalError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"{message} at line {line}, column {column}")
        self.line = line
        self.column = column
# Manejo de errores Sintacticos
class ParsingError(Exception):
    def __init__(self, message, line, column):
        super().__init__(f"{message} at line {line}, column {column}")
        self.line = line
        self.column = column
class SemanticError(Exception):
    def __init__(self, message):
        super().__init__(message)      
# Implementacion
class CompiScriptVisitor(CompiScriptLanguageVisitor):
    def __init__(self) -> None:
        super().__init__()
        # Tabla de simbolos por ambito entonces por cada ambito (contexto) habra una tabla de simbolos
        self.TablaDeAmbitos = HashMap()
        self.stackAmbitos = Stack([0])
        self.currentFuncion = None
        self.classDeclarationName = None
        self.insideVariable = None
        
    def instanciarUnaClase(self, ctx, nombreClase):
        # Chequear en la tabla de tipos en el context y si no existe generar error
        if self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.get(nombreClase) == None:
            raise SemanticError(f"Error semantico, no existe la clase \"{nombreClase}\"")
        metodoInit:Metodo = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(nombreClase+".init")
        # Puede que no tengan init por lo que se cheque y en caso de que no tenga init entonces solo se pasa
        if metodoInit!= None:
            newTablaSimbolos = HashMap()
            mapa = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.map
            newTablaSimbolos.replaceMap(mapa)
            arguments = []
            if len(ctx.arguments())>0:
                arguments = self.visit(ctx.arguments()[0])
            # Meter los parametros que se usan en esa inicializacion, si no son de igual length entonces raise error
            if len(arguments) != len(metodoInit.parametros):
                raise SemanticError(f"Error Semantico, se esperaban {len(metodoInit.parametros)} parametros, {len(arguments)} fueron recibidos")
            index = 0
            for argument in arguments:
                parametro = metodoInit.parametros[index]
                tempP = self.visit(argument)
                newTablaSimbolos.put(parametro, Parametro(parametro, tempP, self.TablaDeAmbitos.size()+1, funcionPertenece=nombreClase+".init"))
                index+=1
            # Crear un nuevo ambito solo para crear los tipos de la clase
            newAmbito:Ambito = Ambito(self.TablaDeAmbitos.size(), newTablaSimbolos)
            newAmbito.tablaDeTipos.replaceMap(self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.map)
            self.stackAmbitos.insert(self.TablaDeAmbitos.size())
            self.TablaDeAmbitos.put(self.TablaDeAmbitos.size(), newAmbito)
            # Visitar el contexto del ambito
            self.visit(metodoInit.contexto)
            # Ahora hay que meter los valores generados en el contexto original
            atributos = newAmbito.tablaDeSimbolos.search(
                r'^' + re.escape(self.variableEnDefinicion) + r'\..*'
            )
            self.stackAmbitos.remove_first()
            for nombreAtributo in atributos:
                atributo = newAmbito.tablaDeSimbolos.get(nombreAtributo)
                self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(nombreAtributo, atributo)
        self.classDeclarationName = None
        self.insideVariable = None
        return self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.get(nombreClase)
        
    def ejecutarFuncionOMetodo(self, ctx, funcionIdentifier):
        newTablaSimbolos = HashMap()
        mapa = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.map
        newTablaSimbolos.replaceMap(mapa)
        arguments = []
        if len(ctx.arguments())>0:
            arguments = self.visit(ctx.arguments()[0])
        # Meter los parametros que se usan en esa inicializacion, si no son de igual length entonces raise error
        if len(arguments) != len(funcionIdentifier.parametros):
            raise SemanticError(f"Error Semantico, se esperaban {len(funcionIdentifier.parametros)} parametros, {len(arguments)} fueron recibidos")
        index = 0
        for argument in arguments:
            parametro = funcionIdentifier.parametros[index]
            tempP = self.visit(argument)
            if isinstance(tempP, Simbolo):
                tempP = tempP.tipo
            newTablaSimbolos.put(parametro, Parametro(parametro, tempP, self.TablaDeAmbitos.size()+1, funcionPertenece=funcionIdentifier.nombreSimbolo))
            index+=1
        # Crear un nuevo ambito solo para almacenar los parametros de la funcion
        newAmbito:Ambito = Ambito(self.TablaDeAmbitos.size(), newTablaSimbolos)
        newAmbito.tablaDeTipos.replaceMap(self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.map)
        self.stackAmbitos.insert(self.TablaDeAmbitos.size())
        self.TablaDeAmbitos.put(self.TablaDeAmbitos.size(), newAmbito)
        # Visitar el contexto del ambito y generar el retorno en caso tenga
        retorno = self.visit(funcionIdentifier.contexto)
        self.stackAmbitos.remove_first()
        return retorno if retorno!=None else Nil()
    
    def imprimirTablaDeSimbolos(self):
        llaves = self.TablaDeAmbitos.keys()
        for llave in llaves:
            ambito:Ambito = self.TablaDeAmbitos.get(llave)
            print(f'''ambito: {ambito.identificadorAmbito}''')
            keys = ambito.tablaDeSimbolos.keys()
            for key in keys:
                symbol:Simbolo
                symbol = ambito.tablaDeSimbolos.get(key)
                print(f'''
                  nombre simbolo: {symbol.nombreSimbolo}    ambito del simbolo: {symbol.ambito}     tipo del simbolo: {symbol.tipo}
                  ''')
    # Visit a parse tree produced by CompiScriptLanguageParser#program.
    def visitProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        if (self.TablaDeAmbitos.size()==0):
            # Crear el contexto main que seria el contexto 0
            self.TablaDeAmbitos.put(0, Ambito(0, HashMap()))
            for child in ctx.declaration():
                self.visit(child)
        # En cualquier otro caso es que se esta dentro de un block que  puede ser declarado como un bloque o como una funcion
        else:
            # De manera que recorrer la declaracion sirve para declarar parametros o demas cosas dentro del ambito del bloque o funcion
            for child in ctx.declaration():
                self.visit(child)

    # Visit a parse tree produced by CompiScriptLanguageParser#classDecl.
    def visitClassDecl(self, ctx:CompiScriptLanguageParser.ClassDeclContext):
        # Primero voy a hacer sin herencia y sin instanciacion, solo crear el tipo
        className = ctx.IDENTIFIER()[0].symbol.text
        # Se crea en la tabla de simbolos del ambito
        self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.put(className, DefinidoPorUsuario(className, valor="clase"))
        # Significa que hay un extends
        classNameExtends = None
        if (len(ctx.IDENTIFIER())>1):
            claseExtendida = ctx.IDENTIFIER()[1].symbol.text
            # Verificar que existe la clase
            # Ir a buscar la clase y verificar que existe, si no existe lanzara error
            classNameExtends = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.get(claseExtendida)
            # Es un tipo definido por usuario si es una clase, si no para ese contexto es otra cosa y se debe lanzar error
            if isinstance(classNameExtends, DefinidoPorUsuario):
                self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.get(className).setInheritance(claseExtendida)
                # Obtener el contexto de la funcion de init de la clase extendida y ponerla dentro de la clase definida por el usuario
                # Obtener los metodos de la clase heredada y meterla como metodos de la clase extendida
                metodos = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.search(classNameExtends.nombreTipo)
                for method in metodos:
                    if method.split('.')[1]!='init':
                        self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(f'{className}.{method.split('.')[1]}', self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(method))
            else:
                raise SemanticError(f'Error semantico, la clase heredada \"{claseExtendida}\" no existe')
        self.classDeclarationName = className
        # Va a visitar todas las funciones
        for child in ctx.function():
            self.visit(child)
        self.TablaDeAmbitos.map[self.stackAmbitos.first()].tablaDeTipos = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos
        self.classDeclarationName = None


    # Visit a parse tree produced by CompiScriptLanguageParser#funDecl.
    def visitFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        self.visit(ctx.function())


    # Visit a parse tree produced by CompiScriptLanguageParser#varDecl.
    def visitVarDecl(self, ctx:CompiScriptLanguageParser.VarDeclContext):
        id = ctx.IDENTIFIER()
        # Esta mal escrito y no se puede obtener la variable en la definicion de la variable
        if ctx.IDENTIFIER() == None:
            raise SemanticError(f'Error semantico, declaracion de variable invalida')
        id = ctx.IDENTIFIER().symbol.text
        self.variableEnDefinicion = id
        # Averiguaremos el tipo despues y la inicializacion despues
        if self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.contains_key(id):
            raise SemanticError(f"Error semantico, no se puede re declarar una variable ya creada en el ambito, \"{id}\"")
        self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(id, Variable(nombreSimbolo=id, ambito=self.stackAmbitos.first()))
        # En caso de que tenga una expresion, porque puede que sea una variable solo definida sin inicializar
        if ctx.expression():
            # Obtener tipo
            variableTipo = self.visit(ctx.expression())
            if isinstance(variableTipo, Simbolo):
                variableTipo = variableTipo.tipo
            # Inicializar la variable y definir el tipo porque al principio es nil
            simbolo:Variable = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(id) 
            simbolo.definirInicializador(variableTipo)
            simbolo.redefinirTipo(variableTipo)
        self.variableEnDefinicion = None
            

    # Visit a parse tree produced by CompiScriptLanguageParser#exprStmt.
    def visitExprStmt(self, ctx:CompiScriptLanguageParser.ExprStmtContext):
        # Se hace la visita de los hijos completos porque se realiza un chequeo sintactico para verificar que el ; existe
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#forStmt.
    def visitForStmt(self, ctx:CompiScriptLanguageParser.ForStmtContext):
        # Verificar si hay una inicialización de variable en el for
        if ctx.varDecl():
            self.visit(ctx.varDecl())
        elif ctx.exprStmt():
            self.visit(ctx.exprStmt())

        # Evaluar la condición del bucle for
        condicion = self.visit(ctx.expression())
        
        # Verificar que la condición sea un booleano
        if not isinstance(condicion, Booleano):
            raise SemanticError(f"Error semántico: la condición del for no es un valor booleano.")
    
        # Ejecutar el bloque del for mientras la condición sea verdadera
        while condicion.valor:  # Asumiendo que `Booleano` tiene un atributo `valor`
            # Visitar el cuerpo del for
            self.visit(ctx.statement())
            
            # Actualizar la expresión de incremento (la tercera parte del for)
            if ctx.expression(1):  # Verifica si hay una expresión de actualización
                self.visit(ctx.expression(1))
            
            # Volver a evaluar la condición después de cada iteración
            condicion = self.visit(ctx.expression())
            
            # Verificar nuevamente que la condición sea un booleano
            if not isinstance(condicion, Booleano):
                raise SemanticError(f"Error semántico: la condición del for no es un valor booleano.")
        
        return None


    # Visit a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def visitIfStmt(self, ctx:CompiScriptLanguageParser.IfStmtContext):
        # Evaluar la expresión condicional
        condicion = self.visit(ctx.expression())
        
        # Verificar que la condición sea un booleano
        if not isinstance(condicion, Booleano):
            raise SemanticError(f"Error semántico: la condición del if no es un valor booleano.")
        
        # Si la condición es verdadera, visitar el bloque del if
        if condicion.valor:  # Asumiendo que `Booleano` tiene un atributo `valor`
            self.visit(ctx.statement(0))
        # Si hay un bloque else y la condición es falsa, visitar el bloque else
        elif ctx.ELSE() is not None:
            self.visit(ctx.statement(1))
        
        # Retornar un valor o continuar la ejecución
        return None


    # Visit a parse tree produced by CompiScriptLanguageParser#printStmt.
    def visitPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        # Just visiting it to make sure it works correctly
        self.visit(ctx.expression())


    # Visit a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def visitReturnStmt(self, ctx:CompiScriptLanguageParser.ReturnStmtContext):
        if (ctx.expression()):
            return self.visit(ctx.expression())
        # Un return solo retorna un nulo
        return Nil(valor=None)


    # Visit a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def visitWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        # Evaluar la expresión condicional del while
        condicion = self.visit(ctx.expression())
        
        # Verificar que la condición sea un booleano
        if not isinstance(condicion, Booleano):
            raise SemanticError(f"Error semántico: la condición del while no es un valor booleano.")
        
        # Ejecutar el bloque del while mientras la condición sea verdadera
        while condicion.valor:  # Asumiendo que `Booleano` tiene un atributo `valor`
            # Visitar el bloque del while
            self.visit(ctx.statement())
            
            # Volver a evaluar la condición después de cada iteración
            condicion = self.visit(ctx.expression())
            
            # Verificar nuevamente que la condición sea un booleano
            if not isinstance(condicion, Booleano):
                raise SemanticError(f"Error semántico: la condición del while no es un valor booleano.")
        
        # Retornar None al final de la ejecución del while
        return None


    # Visit a parse tree produced by CompiScriptLanguageParser#block.
    def visitBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        # Lo unico que puede haber en un bloque es una declaracion pero se tiene que crear un nuevo ambito
        lastDeclaration = None
        # Crear nuevo ambito
        newTablaSimbolos = HashMap()
        mapa = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.map
        newTablaSimbolos.replaceMap(mapa)
        newAmbito:Ambito = Ambito(self.TablaDeAmbitos.size(), newTablaSimbolos)
        newAmbito.tablaDeTipos.replaceMap(self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.map)
        self.stackAmbitos.insert(self.TablaDeAmbitos.size())
        self.TablaDeAmbitos.put(self.TablaDeAmbitos.size(), newAmbito)
        for declarations in ctx.declaration():
            lastDeclaration = self.visit(declarations)            
        # Sale del ambito creado, en caso de una funcion se crean dos ambitos, el externo con la funcion y el interno que es el del bloque
        lastAmbito = self.stackAmbitos.remove_first()
        # Probablemente se este llamando algun metodo
        if self.insideVariable!=None:
            names = []
            if isinstance(self.insideVariable, Simbolo):
                names = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.search(
                    r'^' + re.escape(self.insideVariable.nombreSimbolo) + r'\..*'
                )
            elif isinstance(self.insideVariable, str):
                names = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.search(
                    r'^' + re.escape(self.insideVariable) + r'\..*'
                )                    
            # Copiar los valores definidos en la variable al ambito actual
            for name in names:
                value:Simbolo = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.get(name)
                self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(value.nombreSimbolo, value)
        elif self.variableEnDefinicion!=None:
            # Copiar los valores definidos en la variable al ambito actual
            names = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.search(
                r'^' + re.escape(self.variableEnDefinicion) + r'\..*'
            )
            for name in names:
                value:Simbolo = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.get(name)
                self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(value.nombreSimbolo, value)
        else:
            pass
        # En caso de que no haya nada retorna un Nil
        return Nil(valor=None) if lastDeclaration == None else lastDeclaration


    # Visit a parse tree produced by CompiScriptLanguageParser#expression.
    def visitExpression(self, ctx:CompiScriptLanguageParser.ExpressionContext):
        # Solo es una comparacion logica
        if ctx.logic():
            return self.visit(ctx.logic())
        # Se esta declarando una variable, pero el this solo puede estar en el contexto de un metodo de una clase
        elif self.classDeclarationName!= None and ctx.call() and self.visit(ctx.call())=="this":
            # Crear un nuevo campo
            identificadorCampo = ctx.getChild(2).symbol.text
            if identificadorCampo == None:
                raise SemanticError(f"Error semantico, la variable para definir el campo de la clase no existe")
            newCampo = Campo(self.variableEnDefinicion+"."+identificadorCampo,Nil(), self.stackAmbitos.first(), nombreVariable=self.variableEnDefinicion)
            # Ocurre la asignacion, se obtiene el parametro al que se asigna y su tipo
            retorno = self.visit(ctx.expression())
            if isinstance(retorno, Parametro) or isinstance(retorno, Variable) or isinstance(retorno, Campo):
                newCampo.definirInicializador(retorno.tipo)
                newCampo.redefinirTipo(retorno.tipo)
            elif isinstance(retorno, Booleano) or isinstance(retorno, Numero) or isinstance(retorno, Cadena) or isinstance(retorno, Nil) or isinstance(retorno, DefinidoPorUsuario):
                newCampo.definirInicializador(retorno.nombreTipo)
                newCampo.redefinirTipo(newCampo.inicializador)
            
            # Se almacena el campo en la tabla de simbolos
            self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(newCampo.nombreSimbolo, newCampo)
        # Re asignacion de una variable dentro de el contexto de un metodo
        elif self.insideVariable!= None and ctx.call() and self.visit(ctx.call())=="this":
            variableName = self.visit(ctx.IDENTIFIER())
            variableValue = self.visit(ctx.expression())
            if isinstance(variableValue, Simbolo):
                variableValue = variableValue
            self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(f'{self.insideVariable.nombreSimbolo}.{variableName}', Simbolo(nombreSimbolo=f'{self.insideVariable.nombreSimbolo}.{variableName}', tipo=variableValue, ambito=self.stackAmbitos.first()))
            pass
        elif ctx.call():
            pass
        # Si no tiene un call y no es logic entonces solo es una reasignacion de variables
        else:
            variableName = self.visit(ctx.IDENTIFIER())
            variableValue = self.visit(ctx.expression())
            self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(variableName, Simbolo(nombreSimbolo=variableValue, tipo=variableValue, ambito=self.stackAmbitos.first()))


    # Visit a parse tree produced by CompiScriptLanguageParser#logic.
    def visitLogic(self, ctx:CompiScriptLanguageParser.LogicContext):
        # En caso de que sea solo un hijo entonces solo sera una comparacion, es decir no es logico la operacion
        if ctx.getChildCount() == 1:
            if type(ctx.comparison())==list:
                for child in ctx.comparison():
                    return self.visit(child)
            else:
                return self.visit(ctx.comparison())
        variable = Booleano()
        for child in ctx.getChildren():
            variableTemp = self.visit(child)
            if variableTemp == 'and' or variableTemp == 'or':
                pass
            elif not isinstance(variableTemp, Booleano) or not isinstance(variable, Booleano):
                raise SemanticError(f'Error semantico, las comparaciones no generan valores booleanos para operar logicamente')
        return variable


    # Visit a parse tree produced by CompiScriptLanguageParser#comparison.
    def visitComparison(self, ctx:CompiScriptLanguageParser.ComparisonContext):
        # En caso de que sea solo un hijo entonces solo sera un term
        if ctx.getChildCount() == 1:
            if type(ctx.term())==list:
                for child in ctx.term():
                    return self.visit(child)
            else:
                return self.visit(ctx.term())
        currentOperation = ''
        variable = None
        for index in range(0, ctx.getChildCount()):
            # variable o valor
            variableTemp = self.visit(ctx.getChild(index))
            # Es una variable
            if isinstance(variableTemp, Variable) or isinstance(variableTemp, Parametro) or isinstance(variableTemp, Campo):
                variableTemp = variableTemp.tipo
            # Es operacion
            if isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='>' or variableTemp=='<' or variableTemp=='>=' or variableTemp=='<=' or variableTemp=='==' or variableTemp=='!=':
                currentOperation = variableTemp
            # Siempre devolvera o generar un booleano al ser comparacion, tienen que ser del mismo tipo
            elif (type(variableTemp)==type(variable)) and (currentOperation=='>' or currentOperation=='<' or currentOperation=='>=' or currentOperation=='<='):
                variable = Booleano()
            # Puede comparar cualquier tipo para ver si son iguales o no
            elif currentOperation=='!=' or currentOperation == '==':
                variable = Booleano()
            elif currentOperation == '' and variable == None:
                variable = variableTemp
            elif currentOperation == '':
                pass
            else:
                raise SemanticError(f'Error semantico, operacion invalida no se pueden comparar diferentes tipos')
        # Retorna el ultimo valor que obtiene la variable luego de operar
        return variable

    # Visit a parse tree produced by CompiScriptLanguageParser#term.
    def visitTerm(self, ctx:CompiScriptLanguageParser.TermContext):
        # En caso de que sea solo un hijo entonces solo sera un factor
        if ctx.getChildCount() == 1:
            if type(ctx.unary())==list:
                for child in ctx.unary():
                    return self.visit(child)
            else:
                return self.visit(ctx.unary())
        # En caso de que sea mas de un hijo probablemente sea una operacion aritmetica o un string
        # Averiguar el tipo de operacion es imperativo por lo que son los pares
        currentOperation = ''
        variable = None
        for index in range(0, ctx.getChildCount()):
            # variable o valor
            variableTemp = self.visit(ctx.getChild(index))
            # Es un simbolo
            if isinstance(variableTemp, Simbolo):
                variableTemp = variableTemp.tipo
            # Es operacion
            if isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='+' or variableTemp=='-' or variableTemp=='*' or variableTemp=='/' or variableTemp=='%':
                currentOperation = variableTemp
            # Si es suma y es cadena o numero, casteo implicito en caso de que sea string + numero
            elif (isinstance(variable, Numero) or isinstance(variable, Cadena)) and (isinstance(variableTemp, Numero) or isinstance(variableTemp, Cadena)) and currentOperation=='+':
                # Se asigna el valor de numero o cadena
                if isinstance(variable, Cadena) or isinstance(variableTemp, Cadena): 
                    variable = Cadena()
                else:
                    variable = Numero()
            # Si es resta, division, multiplicacion o modulo es numero
            elif  isinstance(variable, Numero) and isinstance(variableTemp, Numero) and (currentOperation=='-' or currentOperation=='/' or currentOperation=='*' or currentOperation=='%'):
                variable = Numero()
            elif currentOperation == '' and variable == None:
                # Es un tipo
                if isinstance(variableTemp, Tipo):
                    variable = variableTemp
                # Es un simbolo
                elif isinstance(variableTemp, Simbolo):
                    variable = variableTemp.tipo
            else:
                raise SemanticError(f'Error semantico, operacion aritmetica invalida (suma, resta, multiplicacion, division), tipo invalido')
        # Retorna el ultimo valor que obtiene la variable luego de operar
        return variable

    # Visit a parse tree produced by CompiScriptLanguageParser#unary.
    def visitUnary(self, ctx:CompiScriptLanguageParser.UnaryContext):
        # En caso de que sea una call que retorne solo el call
        if ctx.call():
            return self.visit(ctx.call())
        # Esto implica que puede negarse el valor o puede volverse negativo
        elif ctx.unary():
            operation = ''
            variable = None
            for child in ctx.getChildren():
                variableTemp = self.visit(child)
                if isinstance(variableTemp, Variable) or isinstance(variableTemp, Parametro) or isinstance(variableTemp, Campo):
                    variableTemp = variableTemp.tipo
                if isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='-':
                    operation = '-'
                elif isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='!':
                    operation = '!'
                elif variable == None and isinstance(variableTemp, Numero) and operation == '-':
                    variable = Numero() 
                elif variable == None and isinstance(variableTemp, Booleano) and operation == '!':
                    variable = Booleano()
                elif isinstance(variable, Numero) and isinstance(variableTemp, Numero) and operation == '-':
                    variable = Numero() 
                elif isinstance(variable, Booleano) and isinstance(variableTemp, Booleano) and operation == '!':
                    variable = Booleano()
                else:
                    raise  SemanticError(f'Error semantico, no se puede negar un no booleano o no se puede poner en negativo un no numero')
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#call.
    def visitCall(self, ctx:CompiScriptLanguageParser.CallContext):
        # en caso de que la cantidad de hijos sea 1 entonces solo es un primary lo que significa que no es una llamada a una funcion
        if ctx.getChildCount() == 1 and isinstance(ctx.getChild(0), CompiScriptLanguageParser.PrimaryContext):
            if type(ctx.primary())==list:
                for child in ctx.primary():
                    return self.visit(child)
            else:
                return self.visit(ctx.primary())
        # Instanciacion de clase como new Perrito()
        elif  self.visit(ctx.getChild(0))=="new":
            # Chequear que no haya IDENTIFIER
            if ctx.IDENTIFIER():
                raise SemanticError("Error semantico, no se pueden buscar metodos o atributos al instanciar una clase")
            # Chequear que solo haya una llamada a argumentos
            if ctx.arguments() and len(ctx.arguments())>1:
                raise SemanticError("Error semantico, no se puede doblar argumentos")
            nombreClase = ctx.getChild(1).getChild(0).symbol.text
            self.classDeclarationName = nombreClase
            return self.instanciarUnaClase(ctx, nombreClase)
        # En caso de que sean argumentos puede que haya algo como funcion().otrafuncion().otrafuncion2() o algo como funcion().identificador o identificadores
        else:                    
            # El primary indicara si el primero es una funcion o una variable
            funcionIdentifier = self.visit(ctx.getChild(0))
            # En caso de que sea funcion
            if isinstance(funcionIdentifier, Funcion):
                newTablaSimbolos = HashMap()
                mapa = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.map
                newTablaSimbolos.replaceMap(mapa)
                arguments = []
                if len(ctx.arguments())>0:
                    arguments = self.visit(ctx.arguments()[0])
                # Meter los parametros que se usan en esa inicializacion, si no son de igual length entonces raise error
                if len(arguments) != len(funcionIdentifier.parametros):
                    raise SemanticError(f"Error Semantico, se esperaban {len(funcionIdentifier.parametros)} parametros, {len(arguments)} fueron recibidos")
                index = 0
                for argument in arguments:
                    parametro = funcionIdentifier.parametros[index]
                    tempP = self.visit(argument)
                    if isinstance(tempP, Simbolo):
                        tempP = tempP.tipo
                    newTablaSimbolos.put(parametro, Parametro(parametro, tempP, self.TablaDeAmbitos.size()+1, funcionPertenece=funcionIdentifier.nombreSimbolo))
                    index+=1
                # Crear un nuevo ambito solo para almacenar los parametros de la funcion
                newAmbito:Ambito = Ambito(self.TablaDeAmbitos.size(), newTablaSimbolos)
                newAmbito.tablaDeTipos.replaceMap(self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.map)
                self.stackAmbitos.insert(self.TablaDeAmbitos.size())
                self.TablaDeAmbitos.put(self.TablaDeAmbitos.size(), newAmbito)
                # Visitar el contexto del ambito y generar el retorno en caso tenga
                funcionIdentifier = self.visit(funcionIdentifier.contexto)
                self.stackAmbitos.remove_first()
            # En caso de que sea algo como funcion().algo o de que sea variable.algo entonces se hace un for para recorrer lo que no es el primary ni el primer set de argumentos
            if len(ctx.arguments())>1 or ctx.IDENTIFIER():
                # vamos a obtener el valor, puede ser un atributo de la clase, o puede ser un metodo
                # De manera que lo mejor es hacer un while para recorrer child por child e ir decidiendo que ocurre
                # Los casos son: .metodo(), .atributo, no puede haber .funcion() porque tiene que ser si o si una funcion dado que se retorna algo, y no puede ser variable porque se obtiene algo por lo que es un atributo
                lastWasInstance = False
                lastVariableValue = None 
                index = 1
                if funcionIdentifier!="this":
                    self.insideVariable = funcionIdentifier
                while index < ctx.getChildCount():
                    child = ctx.getChild(index)
                    lastVariableValue = self.visit(child)
                    if isinstance(lastVariableValue, str) and not lastVariableValue == ".":
                        # Si retorna this chequear que tiene un . la definicion
                        if funcionIdentifier == "this":
                            lastVariableValue = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(f'{self.insideVariable.nombreSimbolo}.{lastVariableValue}')
                        elif isinstance(funcionIdentifier, Nil):
                            pass
                        # Buscar si existe el coso .variable
                        elif isinstance(funcionIdentifier.tipo, DefinidoPorUsuario):
                            lastVariableValue = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(f'{funcionIdentifier.tipo.nombreTipo}.{lastVariableValue}')
                            if lastVariableValue == None:
                                raise SemanticError(f"Error Semantico, no existe el atributo o metodo {lastVariableValue}")
                        pass
                        
                    # Si el token es un punto se ignora
                    if isinstance(lastVariableValue, TerminalNodeImpl) and lastVariableValue.getText() == "." or lastVariableValue == ".":
                        pass
                    # Si es un metodo se ejecuta el metodo
                    elif isinstance(lastVariableValue, Metodo):
                        newTablaSimbolos = HashMap()
                        mapa = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.map
                        newTablaSimbolos.replaceMap(mapa)
                        arguments = []
                        # Obtener los argumentos
                        # sumarle 1 al index para obtener los argumentos
                        index+=1
                        hijo = ctx.getChild(index)
                        while self.visit(hijo)!=')':
                            index+=1
                            # Si es un argumento lo que se obtiene
                            if isinstance(hijo, CompiScriptLanguageParser.ArgumentsContext):
                                arguments.extend(self.visitArguments(hijo))
                            hijo = ctx.getChild(index)                            
                        # Meter los parametros que se usan en esa inicializacion, si no son de igual length entonces raise error
                        if len(arguments) != len(lastVariableValue.parametros):
                            raise SemanticError(f"Error Semantico, se esperaban {len(lastVariableValue.parametros)} parametros, {len(arguments)} fueron recibidos")
                        index2 = 0
                        for argument in arguments:
                            parametro = lastVariableValue.parametros[index2]
                            tempP = self.visit(argument)
                            if isinstance(tempP, Simbolo):
                                tempP = tempP.tipo
                            newTablaSimbolos.put(parametro, Parametro(parametro, tempP, self.TablaDeAmbitos.size()+1, funcionPertenece=lastVariableValue.nombreSimbolo))
                            index2+=1
                        # Crear un nuevo ambito solo para almacenar los parametros de la funcion
                        newAmbito:Ambito = Ambito(self.TablaDeAmbitos.size(), newTablaSimbolos)
                        newAmbito.tablaDeTipos.replaceMap(self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.map)
                        self.stackAmbitos.insert(self.TablaDeAmbitos.size())
                        self.TablaDeAmbitos.put(self.TablaDeAmbitos.size(), newAmbito)
                        # Visitar el contexto del ambito y generar el retorno en caso tenga
                        retorno = self.visit(lastVariableValue.contexto)
                        self.stackAmbitos.remove_first()
                        funcionIdentifier = retorno
                        # return retorno if retorno!=None else Nil()
                    # En caso de que sea una variable hay que chequear los siguientes
                    elif isinstance(funcionIdentifier, Variable) or isinstance(funcionIdentifier, Campo) or isinstance(funcionIdentifier, Parametro):
                        lastVariableValue = funcionIdentifier
                    index+=1
            return funcionIdentifier if funcionIdentifier!=None else Nil()


    # Visit a parse tree produced by CompiScriptLanguageParser#primary.
    def visitPrimary(self, ctx:CompiScriptLanguageParser.PrimaryContext):
        # Primary es el tipo basico, puede ser casi cualquier cosa, una expresion, una definicion de variable, etc
        # En este caso puede ser una expresion, o super.IDENTIFIER entonces este se tiene que encargar del identifier
        if not ctx.expression() and ctx.getChildCount()>1:
            # Es un super, hay que chequear que se esta inicializando o se esta trabajando dentro de una clase
            if self.classDeclarationName!= None and self.visit(ctx.getChild(0)) == "super":
                # Ejecutar la funcion del super
                # Buscar la clase que se esta inicializando
                claseInicializando:DefinidoPorUsuario = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.get(self.classDeclarationName)
                # Retornar la funcion a ejecutar -> heredada
                return self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(f'{claseInicializando.inheritance}.{ctx.getChild(2)}')
        # Es una variable o es un super.IDENTIFIER hay que buscarlo en la tabla de simbolos
        if ctx.IDENTIFIER():
            id = ctx.IDENTIFIER().symbol.text
            ambitoActual:Ambito = self.TablaDeAmbitos.get(self.stackAmbitos.first())
            tablaDeTiposActual:HashMap = ambitoActual.tablaDeTipos
            tablaDeSimbolosActual:HashMap = ambitoActual.tablaDeSimbolos
            # Puede retornar una variable o el nombre de una funcion
            if (tablaDeSimbolosActual.get(id)== None and tablaDeTiposActual.get(id)==None):
                raise SemanticError(f"Error semantico la variable, la clase o la funcion \"{id}\" no existe")
            return tablaDeSimbolosActual.get(id)
        # Tipo numero
        elif ctx.NUMBER():
            return Numero()
        # Tipo string
        elif ctx.STRING():
            return Cadena()
        # Tipo booleano
        elif ctx.getText() == "false" or ctx.getText() == "true":
            return Booleano()
        # Tipo booleano
        elif ctx.getText() == "nil":
            return Nil()
        # Expresion a resolver
        elif ctx.expression():
            return self.visit(ctx.expression())
        # Acceder a un valor para asignarlo o desde un metodo para hacer algo con el
        elif ctx.getText() == "this":
            return "this"
        elif ctx.getText() == "super":
            # instanciate the super method in the class, searching the inheritance 
            return "super"
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#function.
    def visitFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        nombreFuncion = ctx.IDENTIFIER().symbol.text
        funcion = None
        # En caso de que no se este declarando una clase
        if (self.classDeclarationName==None):
            self.currentFuncion = nombreFuncion
            funcion = Funcion(nombreFuncion, TipoFuncion(), self.stackAmbitos.first())
        # Metodos de una clase
        else:
            nombreFuncion = self.classDeclarationName+"."+nombreFuncion
            # en este caso basicamente solo hay que obtener los fields de la clase
            funcion = Metodo(nombreSimbolo=nombreFuncion, tipo=TipoFuncion(), ambito=self.stackAmbitos.first())
        # Si la funcion/metodo tiene parametros
        if ctx.parameters():
            # Obtener los parametros y meterlos en la tabla de simbolos actual no la de la funcion para desglosar la funcion
            parametros = self.visit(ctx.parameters())
            for parametro in parametros:
                # Solamente almacenar el parametro en la funcion
                funcion.aniadirParametro(parametro)
        # Solamente se va a almacenar el contexto de la ejecucion de la funcion
        funcion.aniadirContexto(ctx.block())
        # Agregar la funcion al ambito actual de la tabla de simbolos
        self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(nombreFuncion, funcion)
            
        
    # Visit a parse tree produced by CompiScriptLanguageParser#parameters.
    def visitParameters(self, ctx:CompiScriptLanguageParser.ParametersContext):
        # Esta visita de parametros solo se puede hacer cuando se instancia la funcion
        if ctx.IDENTIFIER():
            if ctx.getChildCount()>1:
                if type(ctx.IDENTIFIER()) == list:
                    parametros = []
                    for parametro in ctx.IDENTIFIER():
                        # Aniadir el parametro a la lista para instanciarlo en el contexto superior de funcion
                        parametros.append(parametro.symbol.text)
                    # retornar el array con los parametros
                    return parametros
            else:
                # retornar un array con el unico parametro
                return [ctx.getChild(0).symbol.text]
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#arguments.
    def visitArguments(self, ctx:CompiScriptLanguageParser.ArgumentsContext):
        arguments = []
        for child in ctx.getChildren():
            if isinstance(child, CompiScriptLanguageParser.ExpressionContext):
                arguments.append(child)
            else:
                self.visit(child)
        return arguments
    
    # Encontrar nodos de error
    def visitErrorNode(self, node: ErrorNode):
        # Lanzar errores
        raise ParsingError(f"Syntax error, encountered: {node.getText()}", node.symbol.line, node.symbol.column)
    
    # Chequeo para verificar si es o no un nodo malformado
    def visitTerminal(self, node):
        # Verifica si el token es malformado
        if node.symbol.type == CompiScriptLanguageParser.MALFORMED:
            line = node.symbol.line
            column = node.symbol.column
            raise LexicalError(f"Unrecognized token '{node.getText()}'", line, column)
        # Continua con la visita normal
        self.visitChildren(node)
        return node.symbol.text