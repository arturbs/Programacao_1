#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#A Primeira Letra em Caixa Alta

def char_unico(string):
	for n in range(len(string)):
		contador = 0
		for i in range(len(string)):
			if string[n] == string[i]:
				contador += 1
		if contador == 1:
			return string[n]


