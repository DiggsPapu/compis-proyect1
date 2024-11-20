.data
.text
countToTen:
li $t2, 0  # Assign 0 to i
li $t2, 0  # Assign 0 to i
L0:
li $t4, 10  # Cargar literal 10
slt $t0, $t2, $t4  # $t0 = (i < 10)
bne $t0, $zero, L1  # Conditional jump
j L2
L1:
move $a0, $t2  # Mover valor de i a $a0
li $v0, 1  # syscall para imprimir entero
syscall
li $t4, 1  # Cargar literal 1
add $t1, $t2, $t4  # $t1 = i + 1
move $t2, $t1  # Assign $t1 to i
move $t2, $t2  # Assign i to i
j L0
L2:
# End of function
lw $ra, 4($sp)  # Restore return address
lw $fp, 0($sp)  # Restore frame pointer
addiu $sp, $sp, 8  # Adjust stack pointer
jr $ra  # Return to caller
main:
jal countToTen  # Saltar a la direccion de la funcion
# Liberar parametros de la pila
addi $sp, $sp, 0  # Ajustar la pila para 0 parámetros