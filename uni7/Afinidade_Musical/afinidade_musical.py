#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Conta Alertas do Açude


def tem_afinidade(l1, l2):
	cont = 0
	for n in range(len(l1)):
		for e in range(len(l2)):
			if l1[n] == l2[e]:
				cont += 1
	if cont >= 3:
		return True
	else:
		return False
