print("Digite o valor de A:")
texto_de_a_digitado = input()
if texto_de_a_digitado == "True":
    A = True
else:
    A = False

print("Digite o valor de B:")
texto_de_b_digitado = input()
B = False # O valor padrão de B será False.
if texto_de_b_digitado == "True":
    B = True

expressao = A and B
print("O resultado de A AND B =", expressao)