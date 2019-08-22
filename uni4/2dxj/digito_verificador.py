# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Calcula DV

numero = raw_input()
numero_par = 0
numero_impar = 0

for n in range(len(numero)):
	if int(n) % 2 == 0:
		numero_impar += int(numero[n])
	elif int(n) % 2 != 0:
		numero_par += int(numero[n])
		
formula = (numero_par * numero_impar) % 11
if formula % 11 == 10:
	formula = "X"

print "%s-%s" %(numero, formula)

