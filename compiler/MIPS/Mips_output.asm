main:
li $t3, 1  # Assign 1 to variable
li $t4, 4  # Assign 4 to variable2
mul $t0, $t5, $t6  # $t0 = 1 * 2
div $t7, $t8  # Divide 7 / 4
mflo $t0  # Store result in $t0
mul $t0, $t3, $t4  # $t0 = variable * variable2
# Unhandled operator: %
add $t1, $t0, $t9  # $t1 = $t0 + 3
sub $t1, $t1, $t0  # $t1 = $t1 - $t0
add $t1, $t1, $t0  # $t1 = $t1 + $t0
move $t0, $t1  # Assign $t1 to variable3
# Unhandled operator: >
# Unhandled operator: <
# Unhandled operator: >
# Unhandled operator: <=
# Unhandled operator: <=
# Unhandled operator: >=
# Unhandled operator: >=
move $t0, $t0  # Assign true to variable0
move $t0, $t0  # Assign true to variable5
# Unhandled operator: >
# Unhandled operator: <
# Unhandled operator: >=
# Unhandled operator: <=
# Unhandled operator: >
# Unhandled operator: <
# Unhandled operator: >=
# Unhandled operator: <=
add $t1, $t0, $t4  # $t1 = "string" + variable2
move $t0, $t1  # Assign $t1 to string
# Unhandled operator: ==
# Unhandled operator: !=
# Unhandled operator: ==
# Unhandled operator: !=
# Unhandled operator: ==
# Unhandled operator: !=
# Unhandled operator: >
# Unhandled operator: and
# Unhandled operator: >
# Unhandled operator: >=
# Unhandled operator: and
# Unhandled operator: and
# Unhandled operator: or
# Unhandled TAC operation: $t2 =  - variable2
# Unhandled TAC operation: $t2 =  - variable
mul $t0, $t2, $t5  # $t0 = $t2 * 1
add $t1, $t0, $t2  # $t1 = $t0 + $t2
mul $t0, $t6, $t0  # $t0 = 2 * 8
add $t1, $t0, $t0  # $t1 = 50 + $t0
# Unhandled operator: >=
# Unhandled TAC operation: $t0 = "raul albiol" != string
# Unhandled operator: and
# Unhandled operator: >
# Unhandled TAC operation: $t2 =  ! $t0
# Unhandled TAC operation: $t2 =  ! $t2
# Unhandled TAC operation: $t2 =  ! $t2
# Unhandled TAC operation: $t2 =  ! $t2
# Unhandled TAC operation: $t2 =  ! $t2
# Unhandled TAC operation: $t2 =  ! $t2
# Unhandled TAC operation: $t2 =  ! $t2
# Unhandled TAC operation: $t2 =  ! $t2
# Unhandled TAC operation: $t2 =  ! $t2
# Unhandled TAC operation: $t2 =  ! $t2
# Unhandled TAC operation: $t2 =  ! $t2
# Unhandled TAC operation: $t2 =  ! $t2
# Unhandled TAC operation: $t2 =  ! $t2
move $t0, $t2  # Assign $t2 to variableprueba