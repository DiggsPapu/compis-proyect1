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
        self.TablaDeAmbitos.put(0, Ambito(0, HashMap()))
        self.stackAmbitos = Stack([0])
        self.classDeclarationName = Stack([])
        self.insideFuncion = Stack([])
        self.insideVariable = Stack([])
        self.variableEnDefinicion = Stack([])
        
    def crearUnNuevoAmbito(self):
        newTablaSimbolos = HashMap()
        mapa = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.map
        newTablaSimbolos.replaceMap(mapa)
        newAmbito:Ambito = Ambito(self.TablaDeAmbitos.size(), newTablaSimbolos)
        newAmbito.tablaDeTipos.replaceMap(self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.map)
        self.stackAmbitos.insert(self.TablaDeAmbitos.size())
        self.TablaDeAmbitos.put(self.TablaDeAmbitos.size(), newAmbito)
        
    def instanciarUnaClase(self, ctx, nombreClase):
        # Chequear en la tabla de tipos en el context y si no existe generar error
        if self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.get(nombreClase) == None:
            raise SemanticError(f"Error semantico, no existe la clase \"{nombreClase}\"")
        # Esto solo significaria que esta siendo un temp algo como new Perrito(cos,sen,tan); por lo que se debe de crear una variable temporal que sera borrada
        if self.variableEnDefinicion.first() == None:
            self.variableEnDefinicion.insert("return")
            self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.put(self.variableEnDefinicion.first(), Variable("return", self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.get(nombreClase),self.stackAmbitos.first()))
        metodoInit:Metodo = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(nombreClase+".init")
        # Puede que no tengan init por lo que se cheque y en caso de que no tenga init entonces solo se pasa
        if metodoInit!= None:
            self.crearUnNuevoAmbito()
            arguments = []
            if len(ctx.arguments())>0:
                arguments = self.visit(ctx.arguments()[0])
            # Meter los parametros que se usan en esa inicializacion, si no son de igual length entonces raise error
            if len(arguments) != len(metodoInit.parametros):
                raise SemanticError(f"Error Semantico, para el metodo \"{metodoInit.nombreSimbolo}\" se esperaban {len(metodoInit.parametros)} parametros, {len(arguments)} fueron recibidos")
            index = 0
            for argument in arguments:
                parametro = metodoInit.parametros[index]
                tempP = self.visit(argument)
                if isinstance(tempP, Simbolo):
                    tempP = tempP.tipo
                self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(parametro, Parametro(parametro, tempP, self.TablaDeAmbitos.size()+1, funcionPertenece=nombreClase+".init"))
                index+=1
            # Visitar el contexto del ambito
            self.visit(metodoInit.contexto)
            # En caso de que no sea un temporal
            atributos = []
            if self.variableEnDefinicion.first()!="return":
                # Ahora hay que meter los valores generados en el contexto original
                atributos = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.search(
                    r'^' + re.escape(self.variableEnDefinicion.first()) + r'\..*'
                )
            lastAmbito = self.stackAmbitos.remove_first()
            for nombreAtributo in atributos:
                atributo = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.get(nombreAtributo)
                self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(nombreAtributo, atributo)
        if self.variableEnDefinicion.first()=="return": self.variableEnDefinicion.remove_first()
        self.classDeclarationName.remove_first()
        self.insideVariable.remove_first()
        return self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.get(nombreClase)
        
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
                  nombre simbolo: {symbol.nombreSimbolo}    ambito del simbolo: {symbol.ambito}     tipo del simbolo: {symbol.tipo}     valor del símbolo:{symbol.tipo.valor}
                  ''')
    
    # Visit a parse tree produced by CompiScriptLanguageParser#program.
    def visitProgram(self, ctx:CompiScriptLanguageParser.ProgramContext):
        # Recorrer el programa
        for child in ctx.declaration():
            self.visit(child)

    # Visit a parse tree produced by CompiScriptLanguageParser#classDecl.
    def visitClassDecl(self, ctx:CompiScriptLanguageParser.ClassDeclContext):
        # Primero voy a hacer sin herencia y sin instanciacion, solo crear el tipo
        className = ctx.IDENTIFIER()[0].symbol.text
        self.classDeclarationName.insert(className)
        # Verificar que el nombre de la clase sea unico
        if self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.get(className)!=None:
            raise SemanticError(f"Clase \"{className}\" ya ha sido declarada")
        # Se crea en la tabla de simbolos del ambito
        self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.put(className, DefinidoPorUsuario(nombreTipo=className, valor="clase"))
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
                    methodn = method.split('.')
                    if methodn[1]!='init':
                        oldMethod:Metodo = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(method)
                        newMethod:Metodo = Metodo(f'{className}.{methodn[1]}', oldMethod.tipo, self.stackAmbitos.first())
                        newMethod.contexto = oldMethod.contexto
                        newMethod.parametros = oldMethod.parametros
                        self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(f'{className}.{methodn[1]}', newMethod)
            else:
                raise SemanticError(f'Error semantico, la clase heredada \"{claseExtendida}\" no existe')
        # Va a visitar todas las funciones
        for child in ctx.function():
            self.visit(child)
        self.TablaDeAmbitos.map[self.stackAmbitos.first()].tablaDeTipos = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos
        self.classDeclarationName.remove_first()


    # Visit a parse tree produced by CompiScriptLanguageParser#funDecl.
    def visitFunDecl(self, ctx:CompiScriptLanguageParser.FunDeclContext):
        self.visit(ctx.function())


    # Visit a parse tree produced by CompiScriptLanguageParser#varDecl.
    def visitVarDecl(self, ctx:CompiScriptLanguageParser.VarDeclContext):
        # Esta mal escrito y no se puede obtener la variable en la definicion de la variable
        if ctx.IDENTIFIER() == None:
            raise SemanticError(f'Error semantico, declaracion de variable invalida')
        # Obtener el nombre del simbolo
        id = ctx.IDENTIFIER().symbol.text
        # Setear el tipo de la variable a Nil inicialmente
        variableTipo = Nil()
        # La variable en definicion actual es esa, se setea asi porque puede que hayan mas variables en definicion dentro de esta como en clases
        self.variableEnDefinicion.insert(id)
        # Si ya hay una variable definida entonces se lanza un error de redeclaracion de variable
        if self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.contains_key(id):
            raise SemanticError(f"Error semantico, no se puede re declarar una variable ya creada en el ambito, \"{id}\"")
        if ctx.expression():
            # Obtener tipo
            variableTipo = self.visit(ctx.expression())
            if isinstance(variableTipo, Simbolo):
                variableTipo = variableTipo.tipo
        self.variableEnDefinicion.remove_first()
        # Inicializar la variable y definir el tipo, no hay return
        self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(id,Variable(nombreSimbolo=id,tipo=variableTipo,inicializador=variableTipo))
            

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
        # Verificar que la condición sea un booleano
        if not isinstance(self.visit(ctx.expression(0)), Booleano):
            raise SemanticError(f"Error semántico: la condición del for no es un valor booleano.")
        self.visit(ctx.expression(1))
        self.visit(ctx.block())
        return Nil()
    
    # Visit a parse tree produced by CompiScriptLanguageParser#ifStmt.
    def visitIfStmt(self, ctx:CompiScriptLanguageParser.IfStmtContext):
        # Evaluar la expresión condicional
        condicion = self.visit(ctx.expression())
        # Verificar que la condición sea un booleano
        if not isinstance(condicion, Booleano):
            raise SemanticError(f"Error semántico: la condición del if no es un valor booleano.")
        # Visitar el bloque del if y aniadir el retorno que haya
        retornos = [self.visit(ctx.block(0))]
        # Tiene un else y aniadir un retorno si hay
        if (len(ctx.block())>1):
            retornos.append(self.visit(ctx.block(1)))
        # Retornar los posibles retornos del if
        if len(retornos)>1 and not isinstance(retornos[0], Nil) and not isinstance(retornos[1], Nil): return retornos
        elif len(retornos)==1 and not isinstance(retornos[0], Nil): return retornos[0]
        return Nil()
    
    # Visit a parse tree produced by CompiScriptLanguageParser#printStmt.
    def visitPrintStmt(self, ctx:CompiScriptLanguageParser.PrintStmtContext):
        # Visitarlo para ver que todo este correcto
        self.visit(ctx.expression())
        return Nil()
        
    # Visit a parse tree produced by CompiScriptLanguageParser#returnStmt.
    def visitReturnStmt(self, ctx:CompiScriptLanguageParser.ReturnStmtContext):
        if (ctx.expression()):
            retorno = self.visit(ctx.expression())
            if self.insideFuncion.first()!=None:
                # Aniadir el retorno del return de la funcion para ese contexto
                if isinstance(retorno, list): self.TablaDeAmbitos.get(self.insideFuncion.first()).variableRetorno.extend(retorno)
                else: self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(self.insideFuncion.first()).variableRetorno.append(retorno)
            return retorno
        # Un return solo retorna un nulo
        return Nil(valor='nil')


    # Visit a parse tree produced by CompiScriptLanguageParser#whileStmt.
    def visitWhileStmt(self, ctx:CompiScriptLanguageParser.WhileStmtContext):
        # Evaluar la expresión condicional del while
        condicion = self.visit(ctx.expression())
        # Verificar que la condición sea un booleano
        if not isinstance(condicion, Booleano):
            raise SemanticError(f"Error semántico: la condición del while no es un valor booleano.")
        # Retornar lo que sea que diga el bloque, solo hay que chequear que lo que haya dentro del statement sea un bloque
        return self.visit(ctx.block())


    # Visit a parse tree produced by CompiScriptLanguageParser#block.
    def visitBlock(self, ctx:CompiScriptLanguageParser.BlockContext):
        # Chequear que este bien hecha la gramática, {} y eso
        if self.visit(ctx.getChild(0))!="{" or self.visit(ctx.getChild(ctx.getChildCount()-1))!="}":raise SemanticError("Error Semantico, el bloque no esta encerrado en llaves")
        # Lo unico que puede haber en un bloque es una declaracion pero se tiene que crear un nuevo ambito
        lastDeclaration = None
        # Crear nuevo ambito
        self.crearUnNuevoAmbito()
        for declarations in ctx.declaration():
            possibleDeclaration = self.visit(declarations)
            if possibleDeclaration!=";":
                lastDeclaration = possibleDeclaration
        # Sale del ambito creado, en caso de una funcion se crean dos ambitos, el externo con la funcion y el interno que es el del bloque
        lastAmbito = self.stackAmbitos.remove_first()
        # Probablemente se este llamando algun metodo
        if self.insideVariable.first()!=None:
            names = []
            if isinstance(self.insideVariable.first(), Simbolo):
                names = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.search(
                    r'^' + re.escape(self.insideVariable.first().nombreSimbolo) + r'\..*'
                )
            elif isinstance(self.insideVariable.first(), str):
                names = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.search(
                    r'^' + re.escape(self.insideVariable.first()) + r'\..*'
                )                    
            # Copiar los valores definidos en la variable al ambito actual
            for name in names:
                value:Simbolo = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.get(name)
                self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(value.nombreSimbolo, value)
        elif self.variableEnDefinicion.first()!=None:
            # Copiar los valores definidos en la variable al ambito actual
            names = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.search(
                r'^' + re.escape(self.variableEnDefinicion.first()) + r'\..*'
            )
            for name in names:
                value:Simbolo = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.get(name)
                self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(value.nombreSimbolo, value)
        else:
            pass
        # En caso de que no haya nada retorna un Nil
        return Nil(valor='nil') if lastDeclaration == None else lastDeclaration


    # Visit a parse tree produced by CompiScriptLanguageParser#expression.
    def visitExpression(self, ctx:CompiScriptLanguageParser.ExpressionContext):
        # Solo es una comparacion logica
        if ctx.logic():
            return self.visit(ctx.logic())
        # Se esta declarando una variable, pero el this solo puede estar en el contexto de un metodo de una clase
        elif self.classDeclarationName.first()!= None and ctx.call() and self.visit(ctx.call())=="this":
            # Crear un nuevo campo
            identificadorCampo = ctx.getChild(2).symbol.text
            if identificadorCampo == None:
                raise SemanticError(f"Error semantico, la variable \"{identificadorCampo}\" para definir el campo de la clase no existe")
            newCampo = Campo(nombreSimbolo=self.variableEnDefinicion.first()+"."+identificadorCampo,tipo=Nil(), ambito=self.stackAmbitos.first(), nombreVariable=self.variableEnDefinicion.first())
            # Ocurre la asignacion, se obtiene el parametro al que se asigna y su tipo
            retorno = self.visit(ctx.expression())
            if isinstance(retorno, Parametro) or isinstance(retorno, Variable) or isinstance(retorno, Campo):
                newCampo.definirInicializador(retorno.tipo)
                newCampo.redefinirTipo(retorno.tipo)
            elif isinstance(retorno, Booleano) or isinstance(retorno, Numero) or isinstance(retorno, Cadena) or isinstance(retorno, Nil) or isinstance(retorno, DefinidoPorUsuario):
                newCampo.definirInicializador(retorno)
                newCampo.redefinirTipo(newCampo.inicializador)
            
            # Se almacena el campo en la tabla de simbolos
            self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(newCampo.nombreSimbolo, newCampo)
        # Re asignacion de una variable dentro de el contexto de un metodo
        elif self.insideVariable.first()!= None and ctx.call() and self.visit(ctx.call())=="this":
            variableName = self.visit(ctx.IDENTIFIER())
            variableValue = self.visit(ctx.expression())
            if isinstance(variableValue, Simbolo):
                variableValue = variableValue.tipo
            self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(f'{self.insideVariable.first().nombreSimbolo}.{variableName}', Campo(nombreSimbolo=f'{self.insideVariable.first().nombreSimbolo}.{variableName}', tipo=variableValue, ambito=self.stackAmbitos.first()))
        elif ctx.call():
            pass
        # Si no tiene un call y no es logic entonces solo es una reasignacion de variables
        else:
            variableName = self.visit(ctx.IDENTIFIER())
            variableValue = self.visit(ctx.expression())
            self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(variableName, Variable(nombreSimbolo=variableValue, tipo=variableValue, ambito=self.stackAmbitos.first()))


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
            # Probablemente sea producto de un if y un else, entonces hay que chequear si alguno de sus valores es booleano y si no lanzar error
            if isinstance(variable, list):
                for var in variableTemp:
                    if isinstance(var, Simbolo):
                        var = var.tipo
                    if isinstance(var, Booleano):
                        variableTemp = var
                        break
            if variableTemp == 'and' or variableTemp == 'or':
                variable.valor = f'{variable.valor}{variableTemp}'
            elif not isinstance(variableTemp, Booleano) or not isinstance(variable, Booleano):
                raise SemanticError(f'Error semantico, las comparaciones no generan valores booleanos para operar logicamente')
            else:
                variable.valor = f'({variable.valor}{variableTemp.valor})'
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
            acceptance = False
            # En caso de que no se retorne una lista convertirlo a lista para generalizar procedimiento
            if not isinstance(variableTemp, list):
                variableTemp = [variableTemp]
            for var in variableTemp:
                # Es una variable
                if isinstance(var, Variable) or isinstance(var, Parametro) or isinstance(var, Campo): var = var.tipo
                # Es operacion
                if isinstance(var, TerminalNodeImpl) or var=='>' or var=='<' or var=='>=' or var=='<=' or var=='==' or var=='!=':
                    acceptance = True
                    currentOperation = var
                # Siempre devolvera o generar un booleano al ser comparacion, tienen que ser del mismo tipo
                elif (type(var)==type(variable)) and (currentOperation=='>' or currentOperation=='<' or currentOperation=='>=' or currentOperation=='<='):
                    acceptance = True
                    variable = Booleano(valor=f'({variable.valor}{currentOperation}{var.valor})')
                # Puede comparar cualquier tipo para ver si son iguales o no
                elif currentOperation=='!=' or currentOperation == '==':
                    acceptance = True
                    variable = Booleano(valor=f'({variable.valor}{currentOperation}{var.valor})')
                elif currentOperation == '' and variable == None:
                    acceptance = True
                    variable = var
                elif currentOperation == '':
                    acceptance = True
                    pass
            if not acceptance:
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
            # Chequear los posibles valores y si hay alguno valido
            if isinstance(variableTemp, list):
                for var in variableTemp:
                    if isinstance(var, Simbolo):
                        var = var.tipo
                    if isinstance(var, Numero) or isinstance(var, Cadena):
                        variableTemp = var
                        break
                if isinstance(variableTemp, list):
                    raise SemanticError(f'Error semantico, operacion aritmetica invalida (suma, resta, multiplicacion, division), tipo invalido 1')
            # Es un simbolo
            if isinstance(variableTemp, Simbolo):
                variableTemp = variableTemp.tipo
            # Es operacion
            if isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='+' or variableTemp=='-' or variableTemp=='*' or variableTemp=='/' or variableTemp=='%':
                currentOperation = variableTemp
            # Si es suma y es cadena o numero, casteo implicito en caso de que sea string + numero
            elif (isinstance(variable, Numero) or isinstance(variable, Cadena)) and (isinstance(variableTemp, Numero) or isinstance(variableTemp, Cadena)) and currentOperation=='+':
                # Se asigna el valor de numero o cadena
                if isinstance(variable, Cadena) or isinstance(variableTemp, Cadena): variable = Cadena(valor=f'{variable.valor}+{variableTemp.valor}')
                else: variable = Numero(valor=f'({variable.valor}+{variableTemp.valor})')
            # Si es resta, division, multiplicacion o modulo es numero
            elif  isinstance(variable, Numero) and isinstance(variableTemp, Numero) and (currentOperation=='-' or currentOperation=='/' or currentOperation=='*' or currentOperation=='%'):
                variable = Numero(valor=f'({variable.valor}{currentOperation}{variableTemp.valor})')
            elif currentOperation == '' and variable == None:
                # Es un tipo
                if isinstance(variableTemp, Tipo):variable = variableTemp
                # Es un simbolo
                elif isinstance(variableTemp, Simbolo):variable = variableTemp.tipo
            else:
                raise SemanticError(f'Error semantico, operacion aritmetica invalida (suma, resta, multiplicacion, division), tipo invalido')
        # Retorna el ultimo valor que obtiene la variable luego de operar
        return variable

    # Visit a parse tree produced by CompiScriptLanguageParser#unary.
    def visitUnary(self, ctx:CompiScriptLanguageParser.UnaryContext):
        # En caso de que sea una call que retorne solo el call
        if ctx.call():return self.visit(ctx.call())
        # Esto implica que puede negarse el valor o puede volverse negativo
        if ctx.unary():
            operation, variable = None, None
            for child in ctx.getChildren():
                variableTemp = self.visit(child)
                # Obtener el tipo del simbolo
                if isinstance(variableTemp, Variable) or isinstance(variableTemp, Parametro) or isinstance(variableTemp, Campo):variableTemp = variableTemp.tipo
                # Manejo de las operaciones
                if not operation == '!' and (isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='-'):operation = '-'
                elif not operation == '-' and (isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='!'):operation = '!'
                elif isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='-' or isinstance(variableTemp, TerminalNodeImpl) or variableTemp=='!': raise SemanticError(f'Error semantico, no se puede negar un booleano con \'-\' o negar un número con \'!\'')
                # Manejo de los tipos
                elif variable == None and isinstance(variableTemp, Numero) and operation == '-':variable = Numero(valor=f'(-{variableTemp.valor})') 
                elif variable == None and isinstance(variableTemp, Booleano) and operation == '!':variable = Booleano(valor=f'(!{variableTemp.valor})') 
                elif isinstance(variable, Numero) and isinstance(variableTemp, Numero) and operation == '-':variable = Numero(valor=f'(-{variableTemp.valor})')  
                elif isinstance(variable, Booleano) and isinstance(variableTemp, Booleano) and operation == '!':variable = Booleano(valor=f'(!{variableTemp.valor})') 
                else: raise  SemanticError(f'Error semantico, no se puede negar un no booleano o no se puede poner en negativo un no numero')
            # Retornar el tipo de la operacion
            return variable


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
            self.classDeclarationName.insert(nombreClase)
            return self.instanciarUnaClase(ctx, nombreClase)
        # En caso de que sean argumentos puede que haya algo como funcion().otrafuncion().otrafuncion2() o algo como funcion().identificador o identificadores
        else:                    
            # El primary indicara si el primero es una funcion o una variable
            funcionIdentifier = self.visit(ctx.getChild(0))
            # En caso de que sea funcion
            if isinstance(funcionIdentifier, Funcion):
                # Ingreso a una funcion, aniadirla
                self.insideFuncion.insert(funcionIdentifier.nombreSimbolo)
                if isinstance(funcionIdentifier, Metodo):
                    self.classDeclarationName.insert(funcionIdentifier.nombreSimbolo.split(".")[0])
                self.crearUnNuevoAmbito()
                arguments = []
                if len(ctx.arguments())>0:
                    arguments = self.visit(ctx.arguments()[0])
                # Meter los parametros que se usan en esa inicializacion, si no son de igual length entonces raise error
                if len(arguments) != len(funcionIdentifier.parametros):
                    raise SemanticError(f"Error Semantico, para esta funcion \"{funcionIdentifier.nombreSimbolo}\" se esperaban {len(funcionIdentifier.parametros)} parametros, {len(arguments)} fueron recibidos")
                index = 0
                for argument in arguments:
                    parametro = funcionIdentifier.parametros[index]
                    tempP = self.visit(argument)
                    if isinstance(tempP, Simbolo):
                        tempP = tempP.tipo
                    self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(parametro, Parametro(parametro, tempP, self.TablaDeAmbitos.size()+1, funcionPertenece=funcionIdentifier.nombreSimbolo))
                    index+=1
                # Visitar el contexto del ambito y generar el retorno en caso tenga
                self.visit(funcionIdentifier.contexto)
                # Si es un metodo se deben de copiar todos los atributos del metodo por si se modificaron o se crearon
                lastAmbito = self.stackAmbitos.remove_first()
                if isinstance(funcionIdentifier, Metodo):
                    insV = self.variableEnDefinicion.first() if self.variableEnDefinicion.first()!=None else self.insideVariable.first()
                    if isinstance(insV, Simbolo):
                        insV = insV.nombreSimbolo
                    names = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.search(
                            r'^' + re.escape(insV) + r'\..*'
                        )
                    for name in names:
                        value:Simbolo = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.get(name)
                        self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(value.nombreSimbolo, value)
                if isinstance(funcionIdentifier, Metodo):
                    self.classDeclarationName.remove_first()
                self.insideFuncion.remove_first()
                if len(funcionIdentifier.variableRetorno)>1: funcionIdentifier = funcionIdentifier.variableRetorno
                else: funcionIdentifier = funcionIdentifier.variableRetorno[0]
            # En caso de que sea algo como funcion().algo o de que sea variable.algo entonces se hace un for para recorrer lo que no es el primary ni el primer set de argumentos
            if len(ctx.arguments())>1 or ctx.IDENTIFIER():
                # vamos a obtener el valor, puede ser un atributo de la clase, o puede ser un metodo
                # De manera que lo mejor es hacer un while para recorrer child por child e ir decidiendo que ocurre
                # Los casos son: .metodo(), .atributo, no puede haber .funcion() porque tiene que ser si o si una funcion dado que se retorna algo, y no puede ser variable porque se obtiene algo por lo que es un atributo
                lastVariableValue = None 
                index = 1
                if funcionIdentifier!="this":
                    self.insideVariable.first().funcionIdentifier
                while index < ctx.getChildCount():
                    child = ctx.getChild(index)
                    lastVariableValue = self.visit(child)
                    if isinstance(lastVariableValue, str) and not lastVariableValue == ".":
                        # Si retorna this chequear que tiene un . la definicion
                        if funcionIdentifier == "this":
                            lastVariableValue = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(f'{self.insideVariable.first().nombreSimbolo}.{lastVariableValue}')
                            if lastVariableValue==None:
                                raise SemanticError(f"No hay propiedad o metodo {self.visit(child)}")
                        elif isinstance(funcionIdentifier, Nil):
                            pass
                        # Buscar si existe el coso .variable
                        elif isinstance(funcionIdentifier.tipo, DefinidoPorUsuario):
                            lastVariableValue = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(f'{funcionIdentifier.tipo.nombreTipo}.{lastVariableValue}') if self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(f'{funcionIdentifier.tipo.nombreTipo}.{lastVariableValue}')!=None else self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(f'{funcionIdentifier.nombreSimbolo}.{lastVariableValue}')
                            if lastVariableValue == None:
                                    raise SemanticError(f"Error Semantico, no existe el atributo o metodo {lastVariableValue}")
                        pass
                        
                    # Si el token es un punto se ignora
                    if isinstance(lastVariableValue, TerminalNodeImpl) and lastVariableValue.getText() == "." or lastVariableValue == ".":
                        pass
                    # Si es un metodo se ejecuta el metodo
                    elif isinstance(lastVariableValue, Metodo):
                        self.insideFuncion.insert(lastVariableValue.nombreSimbolo)
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
                        self.visit(lastVariableValue.contexto)
                        lastAmbito = self.stackAmbitos.remove_first()
                        # Copiar todos los modificados
                        names = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.search(
                            r'^' + re.escape(self.insideVariable.first().nombreSimbolo) + r'\..*'
                        )
                        for name in names:
                            value:Simbolo = self.TablaDeAmbitos.get(lastAmbito).tablaDeSimbolos.get(name)
                            self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.put(value.nombreSimbolo, value)
                        self.insideFuncion.remove_first()
                        funcionIdentifier = lastVariableValue.variableRetorno # Puede retornar una lista
                    # En caso de que sea una variable hay que chequear los siguientes
                    elif isinstance(lastVariableValue, Variable) or isinstance(lastVariableValue, Campo) or isinstance(lastVariableValue, Parametro):
                        funcionIdentifier = lastVariableValue
                    index+=1
            return funcionIdentifier if funcionIdentifier!=None else Nil(valor="nil")


    # Visit a parse tree produced by CompiScriptLanguageParser#primary.
    def visitPrimary(self, ctx:CompiScriptLanguageParser.PrimaryContext):
        # Primary es el tipo basico, puede ser casi cualquier cosa, una expresion, una definicion de variable, etc
        # En este caso puede ser una expresion, o super.IDENTIFIER entonces este se tiene que encargar del identifier
        if not ctx.expression() and ctx.getChildCount()>1:
            # Es un super, hay que chequear que se esta inicializando o se esta trabajando dentro de una clase
            if (self.classDeclarationName.first()!= None or (self.insideVariable.first()!=None and isinstance(self.insideVariable.first(), DefinidoPorUsuario))) and self.visit(ctx.getChild(0)) == "super":
                # Ejecutar la funcion del super
                # Buscar la clase que se esta inicializando
                claseInicializando:DefinidoPorUsuario = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeTipos.get(self.classDeclarationName.first())
                retorno = self.TablaDeAmbitos.get(self.stackAmbitos.first()).tablaDeSimbolos.get(f'{claseInicializando.inheritance}.{ctx.getChild(2)}')
                if retorno == None:
                    raise SemanticError(f"La super clase \"{ctx.getChild(2)}\" invocada no existe")
                # Retornar la funcion a ejecutar -> heredada
                return retorno
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
            return Numero(valor=ctx.getText())
        # Tipo string
        elif ctx.STRING():
            return Cadena(valor=ctx.getText())
        # Tipo booleano
        elif ctx.getText() == "false" or ctx.getText() == "true":
            return Booleano(valor=ctx.getText())
        # Tipo booleano
        elif ctx.getText() == "nil": return Nil(valor='nil')
        # Expresion a resolver
        elif ctx.expression():
            return self.visit(ctx.expression())
        # Acceder a un valor para asignarlo o desde un metodo para hacer algo con el
        elif ctx.getText() == "this":
            return "this"
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CompiScriptLanguageParser#function.
    def visitFunction(self, ctx:CompiScriptLanguageParser.FunctionContext):
        nombreFuncion = ctx.IDENTIFIER().symbol.text
        funcion = None
        # En caso de que no se este declarando una clase
        if (self.classDeclarationName.first()==None):
            funcion = Funcion(nombreFuncion, TipoFuncion(), self.stackAmbitos.first())
        # Metodos de una clase
        else:
            nombreFuncion = self.classDeclarationName.first()+"."+nombreFuncion
            # en este caso basicamente solo hay que obtener los fields de la clase
            funcion = Metodo(nombreSimbolo=nombreFuncion, tipo=TipoFuncion(), ambito=self.stackAmbitos.first())
        # Si la funcion/metodo tiene parametros
        if ctx.parameters():
            # Obtener los parametros y meterlos en la tabla de simbolos actual no la de la funcion para desglosar la funcion
            parametros = self.visit(ctx.parameters())
            # Solamente almacenar el parametro en la funcion
            for parametro in parametros: funcion.aniadirParametro(parametro)
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