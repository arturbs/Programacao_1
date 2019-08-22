#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamação 1, 2018.2
#Binary Coded Decimal

entrada = 0
binarios = []


while entrada != "fim":
	entrada = raw_input()
	binarios.append(entrada)


for n in range(len(binarios) - 1):
	if len(binarios[n]) < 8:
		print "Tente novamente."
	else:
		if int(binarios[n][0:4], 2) > 9 or int(binarios[n][4:], 2) > 9 :
			print 'BCD inválido.'
		else:
			print "%d%d" %(int(binarios[n][0:4], 2), int(binarios[n][4:], 2))
