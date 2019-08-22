#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Conta Alertas do Açude

def conta_alertas_acude(medicoes):
	alarme = 0
	for n in range(1,len(medicoes)):
		if medicoes[n] < 17 and abs(medicoes[n] - medicoes[n-1]) < 10:
			alarme += 1
	return alarme




