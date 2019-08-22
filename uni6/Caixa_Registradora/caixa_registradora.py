#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Caixa Registradora

def caixa_registradora(lista, meta):
	comissao = 0
	soma = 0
	for n in range(len(lista)):
		if int(lista[n]) < 1000:
			comissao += (int(lista[n]) / 100.0) * 5
			soma += int(lista[n])
		elif int(lista[n]) < 5000:
			comissao += (int(lista[n]) / 100.0) * 10
			soma += int(lista[n])
		else:
			comissao += (int(lista[n]) / 100.0) * 15
			soma += int(lista[n])
	if (soma - comissao) < meta:
		saldo = "Prejuizo"
	else:
		saldo = "Lucro"
	
	
	return [soma, comissao, saldo]

