#coding:utf-8
#Artur Brito Souza - 118210056
#Programação 1 - 17/09/2018
#Economizando a Bolsa de Estudos

mes = 0
valor_mes = 0
mes_acumulado = 0

for n in range (12):
	gastos = int(raw_input())
	valor_mes += (500 - gastos)
	if valor_mes >= mes_acumulado :
		mes_acumulado = valor_mes
		mes_com_conta_maior = n + 1
		
		
if mes_com_conta_maior == 1:
	print "jan"
elif mes_com_conta_maior == 2:
	print "fev"
elif mes_com_conta_maior == 3:
	print "mar"
elif mes_com_conta_maior == 4:
	print "abr"
elif mes_com_conta_maior == 5:
	print "mai"
elif mes_com_conta_maior == 6:
	print "jun"
elif mes_com_conta_maior == 7:
	print "jul"
elif mes_com_conta_maior == 8:
	print "ago"
elif mes_com_conta_maior == 9:
	print "set"
elif mes_com_conta_maior == 10:
	print "out"
elif mes_com_conta_maior == 11:
	print "nov"
elif mes_com_conta_maior == 12:
	print "dez"
	
	
	
	
	
