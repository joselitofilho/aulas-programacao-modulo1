A = True
B = True
resultado = A or (not B)
#print ("A OR (NOT B) =", resultado);

A = False
B = True
resultado = A or (not B)
#print ("A OR (NOT B) =", resultado);

A = False
B = False
resultado = (not A) or B
#print ("(NOT A) OR B =", resultado);

A = True
B = False
resultado = (not A) and B
#print ("(NOT A) AND B =", resultado);

A = True
B = False
resultado = (not A) and (not B)
#print ("(NOT A) AND (NOT B) =", resultado);

A = False
B = False
resultado = not ((not A) and (not B))
#print ("NOT ((NOT A) AND (NOT B)) =", resultado);

A = True
B = True
resultado = not (A and (not B))
#print ("NOT (A AND (NOT B)) =", resultado);
