# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Qualitativa

palavra1 = raw_input()
palavra2 = raw_input()
palavra3 = raw_input()
nova_palavra1 = ""
nova_palavra2 = ""


for i in range(len(palavra1)):
	if palavra1[i] > palavra2[i]:
		nova_palavra1 += palavra1[i]
	elif palavra1[i] == palavra2[i]:
		nova_palavra1 += palavra2[i]
	else:
		nova_palavra1 += palavra2[i]
	if nova_palavra1[i] > palavra3[i]:
		nova_palavra2 += nova_palavra1[i]
	elif nova_palavra1[i] == palavra3[i]:
		nova_palavra2 += palavra3[i]
	else:
		nova_palavra2 += palavra3[i]
    
print nova_palavra2
