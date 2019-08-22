#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Divisor

def divisor(num, lista):
	contador = 0
	for n in range(len(lista)):
		if lista[n] % num == 0:
			contador += 1
			return n
	if contador == 0:
		return -1


