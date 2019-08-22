#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamação 1, 2018.2
#Karel, o Robô

posicao_x = 0
posicao_y = 0

quantidade = 0
direcao = ""


while quantidade  != '0':
	comando = raw_input()
	comando.split()
	direcao, quantidade = comando.split()
	if quantidade == "0":
		print "Fim de jogo"
	if direcao == "c" or direcao == "C":
		posicao_y += int(quantidade)
	elif direcao == "b" or direcao == "B":
		posicao_y -= int(quantidade)
	elif direcao == "e" or direcao == "E":
		posicao_x -= int(quantidade)
	elif direcao == "d" or direcao == "D":
		posicao_x += int(quantidade)
	if abs(posicao_y) == abs(posicao_x) * 2 and posicao_x != 0:
		print "Parabéns, conquista do portal (%d, %d)" %(posicao_x, posicao_y)
		break
		
