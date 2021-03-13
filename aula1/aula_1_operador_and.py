print("Tabela verdade do operador AND")

a_farmacia_vende_remedio = True
a_farmacia_vende_alcool_em_gel = True
print(a_farmacia_vende_remedio and a_farmacia_vende_alcool_em_gel)

a_farmacia_vende_combustivel = False
a_farmacia_vende_remedio = True
print(a_farmacia_vende_combustivel and a_farmacia_vende_remedio)

a_farmacia_vende_cerveja = False
a_farmacia_vende_pao = False
print(a_farmacia_vende_cerveja and a_farmacia_vende_pao)

a_farmacia_vende_remedio = True
a_farmacia_vende_cerveja = False
print(a_farmacia_vende_remedio and a_farmacia_vende_cerveja)