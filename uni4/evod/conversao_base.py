#coding:utf-8
#Artur Brito Souza - 118210056
#Programação 1 - 17/09/2018
#Conversão de Número na Base 2 para a Base 10

binario = int(raw_input())
partes_binario = str(binario)
elevado = len(partes_binario)
decimal = 0

for n in range(len(partes_binario)):
	elevado -= 1
	final = int(partes_binario[n]) * (2 ** elevado)
	print partes_binario[n] + " * " + str((2 ** elevado)) + " = " + str(final)
	decimal += final
	
print "%d(2) = %d(10)" %(binario, decimal)
