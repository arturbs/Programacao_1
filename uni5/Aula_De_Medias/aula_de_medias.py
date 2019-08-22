#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Acima da média (Criminalidade)

somatorio = 0
contador = 0
numeros = []
while somatorio <= 100:
	numero = float(raw_input())
	somatorio += numero
	contador += 1
	numeros.append(numero)

media = somatorio / contador


print "Quantidade de números lidos: %d" %contador
print "Soma dos números lidos: %.2f" %somatorio
print "Média = %.2f" %media

print "\nAbaixo da média"
for n in range(len(numeros)):
	if numeros[n] < media:
		print "%.2f (%do)" %(numeros[n], n + 1)

print ""

print "Acima da média"
for n in range(len(numeros)):
	if numeros[n] > media:
		print "%.2f (%do)" %(numeros[n], n + 1)





