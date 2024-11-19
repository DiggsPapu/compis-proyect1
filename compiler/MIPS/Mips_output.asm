.data
.text
main:
li $t1, 0  # Assign 0 to a
li $v0, 1
move $a0, $t1
syscall
li $t3, 5  # Cargar literal 5
add $t0, $t1, $t3  # $t0 = a + 5
move $t4, $t0  # Assign $t0 to b
li $t1, 15  # Assign 15 to a
add $t0, $t1, $t4  # $t0 = a + b
move $t5, $t0  # Assign $t0 to c
li $v0, 1
move $a0, $t4
syscall
li $v0, 1
move $a0, $t5
syscall