.data
str_Global_Variable_inside_function: .asciiz "Global Variable inside function"
str_$t0: .space 256
.text
main:
li $t1, 20  # Assign 20 to globalVar1
la $t2, str_Global_Variable_inside_function  # Cargar direccion de cadena Global Variable inside function
move $t0, $t2  # Cargar $t2
move $t1, $t1  # Cargar $t1
la $t2, str_$t0  # Cargar dirección para resultado


# Concatenación de cadenas
move $a0, $t0  # Primera cadena
li $v0, 4      # syscall para imprimir cadena
syscall

li $a0, 32     # Cargar el valor ASCII del espacio en blanco en $a0
li $v0, 11     # syscall para imprimir un carácter
syscall        # Llamada al sistema

move $a0, $t1  # Segunda cadena
li $v0, 1      # syscall para imprimir cadena
syscall
move $t0, $t2  # Guardar dirección del resultado en $t0
li $a0, 10
li $v0, 11
syscall
move $a0, $t0  # Mover valor de $t0 a $a0
li $v0, 4  # syscall para imprimir concatenación
syscall
li $a0, 10
li $v0, 11
syscall
move $a0, $t1  # Mover valor de globalVar1 a $a0
li $v0, 1  # syscall para imprimir entero
syscall
li $a0, 10
li $v0, 11
syscall
li $a0, 5  # Cargar valor inmediato 5
li $v0, 1  # syscall para imprimir entero
syscall