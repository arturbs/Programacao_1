# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Conta caracteres inversa

palavra = raw_input()
palavra_inversa = ""
contador = 0

for n in range(len(palavra)-1,-1,-1):
	inversa = palavra[n]
	palavra_inversa += inversa
	
for n in range(len(palavra)):
	if palavra[n] == palavra_inversa[n]:
		contador += 1

print "A palavra %s contém %d caractere(s) coincidente(s) com a sua inversa." %(palavra, contador)
