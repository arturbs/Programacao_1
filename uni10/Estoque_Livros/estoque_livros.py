#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Livros Estoque

def ausentes(estoque):
	ausentes = 0
	quantidades = estoque.values()
	for n in range(len(quantidades)):
		if quantidades[n] == 0:
			ausentes += 1
	return ausentes

livros = { "Metamorfose": 30, "O Principe": 0, "Vigiar e Punir": 0, "Dumbo": 22}
print ausentes(livros)
