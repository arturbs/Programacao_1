#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2

frase = "A vida eh como uma caixa de chcolate, e a vida eh bela"

def bagulho(frase):
	dicionario = {}
	palavras = frase.lower().split(" ")
	for n in range(len(palavras)):
		if dicionario.has_key(palavras[n]):
			dicionario[palavras[n]].append(n)
		else:
			dicionario[palavras[n]] = [n]
		
	for f in range(len(dicionario)):
		print dicionario.keys()[f], ":", dicionario.values()[f]		
	'''modo usando in, que provavelmente não pode usar no miniteste'''
	for key in dicionario:
		print key, ":", dicionario[key] 
	

bagulho(frase)

#coding: utf-8
#Mt_U10
#palavras na frase

def acha_palavras(frase):
    dicio = {}
    palavras = frase.lower().split()
    for n in range(len(palavras)):
        if dicio.has_key(palavras[n]):
            dicio[palavras[n]].append(n)
        else:
            dicio[palavras[n]] = [n]
    return dicio
    
print acha_palavras(frase)

lista1 = [14, 7, 18, 19, 5]


def resumo_numeros(N, lista):
	dicionario = {}
	for n in range(len(lista)):
		if dicionario.has_key(lista[n]%N):
			dicionario[lista[n]%N].append(lista[n])
		else:
			dicionario[lista[n]%N] = [lista[n]]
	return dicionario
	
print resumo_numeros(3, lista1)
