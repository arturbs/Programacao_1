#coding:utf-8
#Artur Brito Souza - 118210056
#Programação 1 - 17/09/2018
#Abaixo da média

valor = raw_input()
lista_de_valores = []

somatorio = 0
contador = 0
while valor != "fim":
	contador += 1
	somatorio += float(valor)
	lista_de_valores.append(valor)
	valor = raw_input()
	if valor == "fim":
		break

media = float(somatorio / contador)
print "%.2f" %media

for variavel in range(len(lista_de_valores)):
	if int(lista_de_valores[variavel]) < media:
		print "%d %d" %((variavel + 1), int(lista_de_valores[variavel]))
