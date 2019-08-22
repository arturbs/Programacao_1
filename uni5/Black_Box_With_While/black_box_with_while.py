
#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamação 1, 2018.2
#Caixa Preta Descartando Leituras

dados = []
peso = 0
combustivel = 0
altura = 0
controle = True

while controle:
	medicoes = raw_input()
	medicoes.split()
	dados_medidos = medicoes.split()
	dados.append(dados_medidos)
	for n in range(len(dados)):
		for i in range(3):
			if float(dados[n][i]) < 0:
				controle = False
				break


for p in range(len(dados)):
	for q in range(1):
		if float(dados[p][q]) >= 0:
			peso += 1
		else:
			break
		if float(dados[p][q+1]) >= 0:
			combustivel += 1
		else:
			break
		if float(dados[p][q+2]) >= 0:
			altura += 1
		else:
			break
			
if peso > combustivel and peso > altura:
	print "dado inconsistente. combustível negativo."
elif peso == combustivel and peso > altura:
	print "dado inconsistente. altitude negativa."
elif peso == combustivel and peso == altura:
	print "dado inconsistente. peso negativo."

print "peso: %d" %(peso)
print "combustível: %d" %(combustivel)
print "altitude: %d" %(altura)

