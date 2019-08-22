#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Ajeita Lista de Números Inteiros

def  agrupa_proximos(lista, valor, criterio):
	proximos = []
	for n in range(len(lista)):
		if abs(lista[n] - valor) < criterio:
			proximos.append(lista[n])
	return proximos
