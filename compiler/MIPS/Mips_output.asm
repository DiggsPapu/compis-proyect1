.data
str_Global_String: .asciiz "Global String"
str_Global_Variable_inside_function: .asciiz "Global Variable inside function"
str_$t0: .space 256
str_is_even.: .asciiz "is even."
.text
main:
li $t2, 10  # Assign 10 to globalVar1
la $t3, str_Global_String  # Load address of string "Global String" into globalVar2
li $t4, 1  # Assign boolean true
li $t2, 20  # Assign 20 to globalVar1
la $t5, str_Global_Variable_inside_function  # Cargar direccion de cadena Global Variable inside function
move $t0, $t5  # Cargar $t5
move $t1, $t2  # Cargar $t2
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
li $a0, 20  # Cargar valor inmediato 20
li $v0, 1  # syscall para imprimir entero
syscall
li $t8, 10  # Cargar literal 10
li $t9, 2  # Cargar literal 2
div $t8, $t9  # Divide 10 by 2
mfhi $t1         # $t1 = 10 % 2 (remainder)
li $t9, 0  # Cargar literal 0
seq $t1, $t1, $t9  # $t1 = ($t1 == 0)
bne $t1, $zero, L1  # Conditional jump
j L0
L1:
li $a0, 10
li $v0, 11
syscall
la $a0, str_is_even.  # Cargar dirección de cadena "is even."
li $v0, 4  # syscall para imprimir cadena
syscall
j L0
L0: