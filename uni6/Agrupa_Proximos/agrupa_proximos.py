#coding: utf -8
#Artur Brito Souza - 118210056
#Programação 1 - 2018.2


import math

def agrupa_proximos(lista, valor, criterio):
	proximos = []
	for n in range(len(lista)):
		distancia = valor - int(lista[n])
		if math.fabs(distancia) < criterio:
			proximos.append(lista[n])
	return proximos
