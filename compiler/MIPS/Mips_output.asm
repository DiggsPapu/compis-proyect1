main:
li $t3, 1  # Assign 1 to variable
li $t4, 4  # Assign 4 to variable2
mul $t0, $t5, $t6  # $t0 = 1 * 2
div $t7, $t8  # Divide 7 / 4
mflo $t0  # Store result in $t0
mul $t0, $t3, $t4  # $t0 = variable * variable2
div $t0, $t8  # Divide $t0 by 4
mfhi $t0         # $t0 = $t0 % 4 (remainder)
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
seq $t0, $t0, $t3  # $t0 = (string == variable)
sne $t0, $t3, $t0  # $t0 = (variable != 20)
seq $t0, $t0, $t0  # $t0 = (50 == 0)
sne $t0, $t0, $t0  # $t0 = ("hola" != 10)
seq $t0, $t0, $t0  # $t0 = (true == false)
sne $t0, $t0, $t0  # $t0 = (true != "demonios")
slt $t0, $t6, $t4  # $t0 = (variable2 > 2)
and $t0, $t0, $t0  # $t0 = $t0 and false
slt $t0, $t6, $t0  # $t0 = (20 > 2)
slt $t0, $t0, $t0  # $t0 = (b < a)
xori $t0, $t0, 1      # $t0 = not($t0)
and $t0, $t0, $t0  # $t0 = $t0 and false
and $t0, $t0, $t0  # $t0 = true and $t0
or $t1, $t0, $t0  # $t1 = $t0 or $t0
neg $t2, $t4  # $t2 = -variable2
neg $t2, $t3  # $t2 = -variable
mul $t0, $t2, $t5  # $t0 = $t2 * 1
add $t1, $t0, $t2  # $t1 = $t0 + $t2
mul $t0, $t6, $t0  # $t0 = 2 * 8
add $t1, $t0, $t0  # $t1 = 50 + $t0
slt $t0, $t1, $t1  # $t0 = (b < a)
xori $t0, $t0, 1      # $t0 = not($t0)