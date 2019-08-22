#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Organiza Lista pela Média

def organiza_por_media(lista):
	media = 0.0
	contador = 0.0
	for n in range(len(lista)):
		media += lista[n]
		contador += 1
	if len(lista) > 0:
		media /= contador
	
	for k in range(len(lista)):
		for j in range(len(lista)-1):
			while(lista[j] > media and not (lista[j+1] > media)):
				lista[j], lista[j+1] = lista[j+1], lista[j]
			
	return lista


