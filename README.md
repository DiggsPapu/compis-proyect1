# Proyecto - Construcción de Compildores
## Índice
- [Descripción](https://github.com/DiggsPapu/compis-proyect1?tab=readme-ov-file#descripci%C3%B3n)
- [Temas vistos](https://github.com/DiggsPapu/compis-proyect1?tab=readme-ov-file#temas-vistos)
- [Organización de archivos](https://github.com/DiggsPapu/compis-proyect1?tab=readme-ov-file#organizaci%C3%B3n-de-archivos)
- [Compilación](https://github.com/DiggsPapu/compis-proyect1?tab=readme-ov-file#compilaci%C3%B3n)
- [Informe](https://github.com/DiggsPapu/compis-proyect1?tab=readme-ov-file#informe)
- [Autores](https://github.com/DiggsPapu/compis-proyect1?tab=readme-ov-file#autores)
  
## Descripción
Para el proyecto se requiere la implementación de un compilador para el legunaje de programación _CompiScript_, donde el objetivo principal es desarrollosar un analizador semántico que verifique y valide las reglas semánticas del lenguaje, incluyendo el manejo de tipos, control de flujo y la resolución ded nombres dentro de diferentes ámbitos.

El compilador deberá tener un IDE interactivo que permita escribir y compilar el código de manera sencilla y visual la cuál sea amigable y facilite la experiencia de usuario.

Dado a que el proceso de compilación de un lenguaje de programación consta de diferentes fases, una de las más importantes es la generación del código intermedio, el cual sirve como un puento entre el análisis semántico y la generación de código de máquina, permitiendo traducir un código fuente de alto nivel a una representación intermedia que sea manejable y optimizada.

## Temas vistos
- CompiScript
- ANTLR
- Analizadores sintácticos
- Árboles sintáctivos abstractos
- Análisis semántico
- Construcción de tabla de símbolos
- Manejo de errores y depuración
- Código intermedio
- Cuadrapletas
- Código de tres direcciones
  
## Organización de archivos
|- compiler

|---- commands

|-------- antlr

|-------- grun

|---- Semantic

|-------- CompiScriptVisitor.py

|-------- Structures.py

|---- Syntax

|-------- CompiScriptLanguage.g4

|-------- CompiScriptLanguage.interp

|-------- CompiScriptLanguage.tokens

|-------- CompiScriptLanguageLexer.interp

|-------- CompiScriptLanguageLexer.py

|-------- CompiScriptLanguageListener.py

|-------- CompiScriptLanguageParser.py

|-------- CompiScriptLanguageVisitor.py

|-------- CompiScriptLexer.interp

|-------- CompiScriptLexer.py

|-------- CompiScriptLexer.tokens

|---- Syntax

|-------- CompiScriptTacVisitor.py

|-------- Structures.py

|---- Textos

|-------- Block.txt

|-------- DeclaracionDeClases.txt

|-------- DeclaracionVariables.txt

|-------- ErroresSintacticos.txt

|-------- Herencia.txt

|-------- Operaciones.txt

|-------- PruebasCompiScript.txt

|-------- pruebasIf.txt

|-------- ReasignacionVariables.txt

|-------- RecursionFibonacci.txt

|---- Dockerfile

|---- Driver.py

|---- parse_tree

|---- parse_tree.dot

|---- Pruebas.py

|---- python-venv.sh

|---- requirements.tx

|- IDE

|---- compiler

|-------- migrations

|-------- static

|-------- templates

|-------- __ init __.py

|-------- admin.py

|-------- apps.py

|-------- models.py

|-------- tests.py

|-------- urls.py

|-------- views.py

|---- compliers_ide

|-------- __ init __.py

|-------- asgi.py

|-------- settings.py

|-------- urls.py

|-------- wsgi.py

|---- db.sqlite3

|---- manage.py

## Compilación
Como primer paso se necesita clonar el repositorio mediante el comando
```bash
git clone https://github.com/DiggsPapu/compis-proyect1.git
```

Posteriormente, cuando ya se tiene el repositorio localmente se tiene que viajar hasta la carpeta donde se encuentra el archivo correspondiente, si se quiere ejecutar el IDE se tiene que trasladar hacia la carpeta donde se encuentra el archivo  `manage.py`, lo cual se hace mediante el comando:
```bash
cd IDE\compilers_ide\
```

Una vez dentro de dicha carpeta hay que correr el archivo en un puerto local, que en este caso será el 800, con el comando: 
```bash
python manage.py runserver
```

Este comando va a inicializar el proyecto de Django, el cual, cuando termine de compilar, va a mostrar un mensaje en la terminal donde se está corriendo el programa que indicará un hipervínculo que abre el IDE del proyecto y que permite utilizarlo.

## Informe
[Informe 1](https://docs.google.com/document/d/1MUOtgfo_JocxVRv28YzvuBl2Zi3Hz35omnp8Z-3jkU0/edit?usp=sharing)

[Informe 2](https://docs.google.com/document/d/1BMCx6oPvcxqTYnhsura5meGajStbzOLjyqDPzApYwNo/edit?usp=sharing)

## Videos
[Video 1](URL)https://youtu.be/ynKdowK_XoY

[Video 2](URL)https://youtu.be/1D3zimnmNrQ

## Autores
Diego Andrés Alonzo Medinilla - 20172

Diana Lucía Fernández Villatoro - 21747
