#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Quantidade de Usuários

def quantidade_usuarios(cadastro):
	contador = 0
	for n in cadastro.keys():
		for l in cadastro[n]:
			if n != 9999:
				contador += 1
	return contador


