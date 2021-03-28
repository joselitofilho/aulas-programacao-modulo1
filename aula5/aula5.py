# -*- coding: utf-8 -*-

print("Escolha a moeda a ser convertida:")
print("Digite 1 para Real R$")
print("Digite 2 para Dólar U$")
print("Digite 3 para Euro €")

moeda_a_ser_convertida = input()

print("A moeda a ser convertida é:", moeda_a_ser_convertida)
#print("A moeda a ser convertida é: %s" % moeda_a_ser_convertida)


print("Qual o valor que você quer converter?")
valor_a_converter = float(input()) # Cast de string para float

print("O valor a converter é:", valor_a_converter)

cotacao_dolar = 5.80
cotacao_euro = 6.70

quantos_euros_eu_tenho = valor_a_converter / cotacao_euro
print("O valor em euros é: %.2f" % quantos_euros_eu_tenho)

quantos_dolares_eu_tenho = valor_a_converter / cotacao_dolar
print("O valor em dolar é: %.2f" % quantos_dolares_eu_tenho)
