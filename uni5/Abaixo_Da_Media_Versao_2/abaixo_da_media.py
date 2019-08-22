#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Abaixo da média

cont = 0 
entrada = 0
valor = []
total = 0

while entrada != 'fim':
	entrada = raw_input()
	valor.append(entrada)
	cont += 1

while cont > 1:
	total += float(valor[cont-2])
	cont -= 1

media = total/(len(valor)-1)
print "%.2f" %media

for n in range(len(valor)-1):
	if int(valor[n]) < media:
		print "%d %s" %(n+1, valor[n]) 
