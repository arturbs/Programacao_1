# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Criptografando uma Senha

palavra = raw_input()
senha = ""
senha += palavra[0]
trocas = 0

for n in range(1,len(palavra)):
	if palavra[n] == "a" or palavra[n] == "A":
		senha += "4"
		trocas += 1
	elif palavra[n] == "e" or palavra[n] == "E":
		senha += "3"
		trocas += 1
	elif palavra[n] == "i" or palavra[n] == "I":
		senha += "1"
		trocas += 1
	elif palavra[n] == "o" or palavra[n] == "O":
		senha += "0"
		trocas += 1
	else:
		senha +=palavra[n]
		
print "%s (%d troca(s))" %(senha, trocas)
