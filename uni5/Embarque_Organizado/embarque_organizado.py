#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamação 1, 2018.2
#Embarque Organizado

lista_de_passageiros = []
lista_par = []
lista_impar = []
embarque = raw_input()
embarque.split()
lista_de_passageiros.append(embarque.split())


for n in range(len(embarque.split())):

	if int(lista_de_passageiros[0][n]) % 2 == 1:
		lista_impar.append(lista_de_passageiros[0][n])
	else:
		lista_par.append(lista_de_passageiros[0][n])

lista_final = lista_impar + lista_par


if lista_final == embarque.split():
	print "ok"
else:
	print "erro"




		 
