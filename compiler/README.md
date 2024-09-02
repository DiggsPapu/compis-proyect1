# compis-proyect1

# Compiling and building env

1. Create a .venv and add requirements
2. Create a docker container (This is just to compile the ANTLR syntax analyzer)

    docker build --rm . -t compis-proyect1 &&
    docker run --rm -ti -v "$(pwd)/Syntax":/Syntax compis-proyect1
    <!-- docker start compis-proyect1
    docker exec -it compis-proyect1 /bin/bash -->

3. Generate ANTLR Syntax Analysis and visitor:
    
    antlr -Dlanguage=Python3 -visitor CompiScriptLanguage.g4 


## Puntos importantes
var es una palabra reservada por ende si se escribiera var var = 20; esto es ilegal.