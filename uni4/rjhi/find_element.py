# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Encontra elemento

procurado = int(raw_input())
sequencia = raw_input()
contador = 0

for n in range(len(sequencia.split())):
	if int(sequencia.split()[n]) == procurado:
		contador += 1

if contador > 0:
	print "sim"
else:
	print "não"
