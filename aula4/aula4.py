print("Digite o valor de A:")
texto_de_a_digitado = input()
A = False # O valor padrão de A será False.
if texto_de_a_digitado == "True":
    A = True
elif texto_de_a_digitado == "Verdadeiro":
	A = True
elif texto_de_a_digitado == "V":
	A = True

print("Digite o valor de B:")
texto_de_b_digitado = input()
B = False # O valor padrão de B será False.
if texto_de_b_digitado == "True":
    B = True
elif texto_de_b_digitado == "Verdadeiro":
	B = True
elif texto_de_b_digitado == "V":
	B = True

expressao = (not A) and (not B)
print("O resultado de A AND B =", expressao)