#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Aplicação Polinômios

mensagem = ""
while mensagem != "fim":
	mensagem = raw_input()
	if mensagem == "fim":
		break
	else:
		if mensagem[0] == "p":
			mensagem.split(":")
			letra, novo_polinomio = mensagem.split(":")
			print "novo polinomio"
		else:
			novo_polinomio.split(" ")
			resultado = 0
			termos = novo_polinomio.split(" ")
			for n in range(1, len(termos)):
				resultado += int(termos[n]) * (int(mensagem) ** (n-1))
			print resultado
