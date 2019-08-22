# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Dígito Verificador de Conta Bancária
import math

numero = raw_input()
dv = 0

for n in range(len(numero)):
	dv += int(numero[n])

if dv % 11 == 10:
	dv = "X"
else:
	dv = dv % 11
		
print "%s-%s" %(numero,str(dv))
	
