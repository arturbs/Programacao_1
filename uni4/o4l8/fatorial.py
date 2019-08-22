# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Fatorial

numero = int(raw_input())
fatorial = 1

for n in range(numero,1,-1):
	fatorial *= n
	
print fatorial
