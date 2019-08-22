# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Classifica Letra como Vogal ou Consoante

palavra = raw_input()

for n in range(len(palavra)):
	if palavra[n] == "a" or palavra[n] == "e" or palavra[n] == "i" or palavra[n] == "o" or palavra[n] == "u":
		print "<%s> sim" %palavra[n]
	elif palavra[n] == "A" or palavra[n] == "E" or palavra[n] == "I" or palavra[n] == "O" or palavra[n] == "U":
		print "<%s> sim" %palavra[n]
	else:
		print "<%s> nao" %palavra[n]


"""if palavra[n] == ("a" or "A") or palavra[n] == ("e" or "E") or palavra[n] == ("i" or "I") or palavra[n] == ("o" or "O") or palavra[n] == ("u" or "U"):"""
