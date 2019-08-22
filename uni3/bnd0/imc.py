# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 15/09/2018 
# Programa :  IMC

peso = float(raw_input())
altura = float(raw_input())

imc = peso / (altura ** 2)

if imc < 16:
	print "IMC: %.1f - Magreza grave" %imc
elif imc < 17:
	print "IMC: %.1f - Magreza moderada" %imc
elif imc < 18.5:
	print "IMC: %.1f - Magreza leve" %imc
elif imc < 25:
	print "IMC: %.1f - Saudável" %imc
elif imc < 30:
	print "IMC: %.1f - Sobrepeso" %imc
elif imc < 35:
	print "IMC: %.1f - Obesidade Grau I" %imc
elif imc < 40:
	print "IMC: %.1f - Obesidade Grau II (severa)" %imc
else:
	print "IMC: %.1f - Obesidade Grau III (mórbida)" %imc
