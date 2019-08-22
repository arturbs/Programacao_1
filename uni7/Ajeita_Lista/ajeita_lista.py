#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Ajeita Lista de Números Inteiros

def ajeita_lista(lista):
	lista_par = []
	lista_impar = []
	
	for e in range(len(lista)):
		if lista[e] % 2 == 0:
			lista_par.append(lista[e])
		else:
			lista_impar.append(lista[e])
			
	
	for n in range(len(lista_par) - 2, -1, -1):
		atual = len(lista_par) -1
		while atual > n:
			if lista_par[n] < lista_par[atual]:
				lista_par[atual], lista_par[n] = lista_par[n], lista_par[atual]
			atual -= 1
			
	for m in range(1, len(lista_impar)):
		atual = 0
		while atual < m:
			if lista_impar[m] < lista_impar[atual]:
				lista_impar[atual], lista_impar[m] = lista_impar[m], lista_impar[atual]
			atual += 1

	
	lista = lista_par + lista_impar
	print lista
	lista1 = lista
				

lista1 = [3, 2, 1, 4, 5, 6, 7, 8, 9]
print ajeita_lista(lista1)
print lista1


