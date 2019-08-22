# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Caixa Preta

"""usuario coloca quantos ciclos de medições o programa deverá ler"""
medicoes = int(raw_input())
med_validas = 0
mensagem = 0

for n in range(medicoes):
	dados = raw_input()
	dados.split()
	peso,combustivel,altitude = dados.split()
	if int(peso) < 0 and mensagem == 0:
		print "dado inconsistente. peso negativo."
		mensagem += 1
	elif mensagem == 0:
		med_validas += 1
	if int(combustivel) < 0 and mensagem == 0:
		print "dado inconsistente. combustível negativo."
		mensagem += 1
	elif mensagem ==0:
		med_validas += 1
	if int(altitude) < 0 and mensagem == 0:
		print "dado inconsistente. altitude negativa."
		mensagem += 1
	elif mensagem == 0:
		med_validas += 1

print "%d dados válidos." %med_validas
		

