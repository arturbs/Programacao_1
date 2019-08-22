#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Acordes aprendidos

def acordes(musica_1, musica_2):
	aprendidos = []
	for i in range(len(musica_1)):
		aprendidos.append(musica_1[i])
	
	for n in range(len(musica_2)):
		contador = 0
		for q in range(len(aprendidos)):
			if musica_2[n] == aprendidos[q]:
				contador += 1
		if contador == 0:
			aprendidos.append(musica_2[n])

	return aprendidos

