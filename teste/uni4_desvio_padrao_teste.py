# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Desvio Padrão
import math

			

sequencia1 = raw_input()
sequencia2 = raw_input()
numero1 = ""
numero2 = ""
soma1 = 0
soma2 = 0
elevado1 = 0
elevado2 = 0
contador1 = 0
contador2 = 0
diferenca1 = 0
diferenca2 = 0
desvio1 = 0
desvio2 = 0

"""o split ira separar os numero que o usuario colocar"""
"""soma1 ira somar todos numeros para poder ser feita a media"""

for n in range(len(sequencia1.split())):
	soma1 += float(sequencia1.split()[n])
	contador1 += 1
if contador1 > 0:
	media1 = soma1 / contador1

for n in range(len(sequencia1.split())):
	diferenca1 = float(sequencia1.split()[n]) - media1 
	elevado1 += diferenca1 ** 2

desvio1 = float(elevado1) / (contador1 - 1)
desvio1 = math.sqrt(desvio1)


for n in range(len(sequencia2.split())):
	soma2 += float(sequencia2.split()[n])
	contador2 += 1
if contador2 > 0:
	media2 = soma2 / contador2

for n in range(len(sequencia2.split())):
	diferenca2 = float(sequencia2.split()[n]) - media2 
	elevado2 += diferenca2 ** 2
	
desvio2 = float(elevado2) / (contador2 - 1)
desvio2 = math.sqrt(desvio2)



if desvio2 > desvio1:
	print "A sequência 2 possui o maior desvio padrão (%.2f)." %desvio2
elif desvio1 > desvio2:
	print "A sequência 1 possui o maior desvio padrão (%.2f)." %desvio1
elif desvio1 == desvio2:
	print "As sequências possuem o mesmo desvio padrão (%.2f)." %desvio2
	


