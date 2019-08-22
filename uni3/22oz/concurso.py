#coding: utf-8
#artur brito souza - 118210056
#UFCG - Programação 1
#Concurso

escrita1 = float(raw_input())
didatica1 = float(raw_input())
titulacao1 = float(raw_input())
idade1 = int(raw_input())

escrita2 = float(raw_input())
didatica2 = float(raw_input())
titulacao2 = float(raw_input())
idade2 = int(raw_input())

media1 = (escrita1 * 0.3) + (didatica1 * 0.4) + (titulacao1 * 0.3)
media2 = (escrita2 * 0.3) + (didatica2 * 0.4) + (titulacao2 * 0.3)

if media1 > media2:
	print "O primeiro candidato foi aprovado com média %.1f." %media1
elif media2 > media1:
	print "O segundo candidato foi aprovado com média %.1f." %media2
elif media1 == media2:
	if idade1 > idade2:
		print "O primeiro candidato foi aprovado com média %.1f." %media1
	elif idade2 > idade1:
		print "O segundo candidato foi aprovado com média %.1f." %media2
	elif idade1 == idade2:
		print "Empate."
