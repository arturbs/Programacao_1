# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Divisores Próprios

numero = int(raw_input())

for n in range(1,numero):
	if numero % n == 0:
		print n
