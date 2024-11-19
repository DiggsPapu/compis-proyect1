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
slt $t0, $t0, $t0  # $t0 = (67890 > 789)
slt $t0, $t0, $t0  # $t0 = (567 < 7890)
slt $t0, $t0, $t3  # $t0 = (variable > variable3)
slt $t0, $t4, $t3  # $t0 = (b > a)
xori $t0, $t0, 1      # $t0 = not($t0)
slt $t0, $t0, $t0  # $t0 = (b > a)
xori $t0, $t0, 1      # $t0 = not($t0)
slt $t0, $t0, $t0  # $t0 = (b < a)
xori $t0, $t0, 1      # $t0 = not($t0)
slt $t0, $t4, $t0  # $t0 = (b < a)
xori $t0, $t0, 1      # $t0 = not($t0)
move $t0, $t0  # Assign true to variable0
move $t0, $t0  # Assign true to variable5
slt $t0, $t0, $t0  # $t0 = (true > false)
slt $t0, $t0, $t0  # $t0 = (false < true)
slt $t0, $t0, $t0  # $t0 = (b < a)
xori $t0, $t0, 1      # $t0 = not($t0)
slt $t0, $t0, $t0  # $t0 = (b > a)
xori $t0, $t0, 1      # $t0 = not($t0)
slt $t0, $t0, $t0  # $t0 = (variable0 > false)
slt $t0, $t0, $t0  # $t0 = (variable0 < true)
slt $t0, $t0, $t0  # $t0 = (b < a)
xori $t0, $t0, 1      # $t0 = not($t0)
slt $t0, $t0, $t0  # $t0 = (b > a)
xori $t0, $t0, 1      # $t0 = not($t0)
add $t1, $t0, $t4  # $t1 = "string" + variable2
move $t0, $t1  # Assign $t1 to string
# Unhandled operator: ==
# Unhandled operator: !=
# Unhandled operator: ==
# Unhandled operator: !=
# Unhandled operator: ==
# Unhandled operator: !=
slt $t0, $t6, $t4  # $t0 = (variable2 > 2)
# Unhandled operator: and
slt $t0, $t6, $t0  # $t0 = (20 > 2)
slt $t0, $t0, $t0  # $t0 = (b < a)
xori $t0, $t0, 1      # $t0 = not($t0)
# Unhandled operator: and
# Unhandled operator: and
# Unhandled operator: or
# Unhandled TAC operation: $t2 =  - variable2
# Unhandled TAC operation: $t2 =  - variable
mul $t0, $t2, $t5  # $t0 = $t2 * 1
add $t1, $t0, $t2  # $t1 = $t0 + $t2
mul $t0, $t6, $t0  # $t0 = 2 * 8
add $t1, $t0, $t0  # $t1 = 50 + $t0
slt $t0, $t1, $t1  # $t0 = (b < a)
xori $t0, $t0, 1      # $t0 = not($t0)
# Unhandled TAC operation: $t0 = "raul albiol" != string
# Unhandled operator: and
slt $t0, $t6, $t5  # $t0 = (1 > 2)
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