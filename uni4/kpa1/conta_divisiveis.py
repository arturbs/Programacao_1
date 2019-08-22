# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Quantidade de Inteiros Divisíveis por K

divisor = int(raw_input())
quantidade = int(raw_input())
contador = 0

for n in range(quantidade):
	numero = int(raw_input())
	if numero % divisor == 0:
		contador +=1

media = (float(contador) / quantidade) * 100

print "%d (%.1f%%)" %(contador, media)
