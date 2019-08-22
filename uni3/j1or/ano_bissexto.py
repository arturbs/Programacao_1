# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  ano bissexto

ano = int(raw_input())

if ano % 400 == 0:
	print "%d é bissexto" %ano
elif ano % 4 == 0 and ano % 100 != 0:
	print "%d é bissexto" %ano
else:
	print "%d não é bissexto" %ano
