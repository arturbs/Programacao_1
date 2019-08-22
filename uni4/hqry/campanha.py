# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Campanha

vitoria = 0
derrotas = 0
empates = 0 
pontos = 0
gols_pro = 0
gols_adversario = 0
saldo = 0
pontos_casa = 0
pontos_fora = 0

for n in range(10):
	partida = raw_input()
	if partida[5] == "c":
		gols_pro += int(partida[0])
		gols_adversario += int(partida[2])
	elif partida[5] == "f":
		gols_adversario += int(partida[0])
		gols_pro += int(partida[2])
	
	if partida[5] == "c" and partida[0] > partida[2]:
		vitoria += 1
		pontos += 3
		pontos_casa += 3 
	elif partida[5] == "c" and partida[0] == partida[2]:
		empates += 1
		pontos += 1
		pontos_casa += 1
	elif partida[5] == "c" and partida[0] < partida[2]:
		derrotas += 1
		pontos += 0
		pontos_casa += 0
	elif partida[5] == "f" and partida[0] < partida[2]:
		vitoria += 1
		pontos += 3
		pontos_fora += 3 
	elif partida[5] == "f" and partida[0] == partida[2]:
		empates += 1
		pontos += 1
		pontos_fora += 1
	elif partida[5] == "f" and partida[0] > partida[2]:
		derrotas += 1
		pontos += 0
		pontos_fora += 0 

saldo = gols_pro - gols_adversario

print "%dv, %de, %dd" %(vitoria, empates, derrotas)
print "pontos: %d" %pontos
print "saldo: %d (%d pro, %d contra)" %(saldo, gols_pro, gols_adversario)
print "pontos em casa: %d" %pontos_casa
print "pontos fora: %d" %pontos_fora

