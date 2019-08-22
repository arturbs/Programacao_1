#coding: utf -8
#Artur Brito Souza - 118210056
#Programação 1 - 2018.2
#Analytics Assembleia

def conta_votos(votacoes,id_votacao):
	contador_sim = 0
	contador_nao = 0 
	for n in range(len(votacoes)):
		voto = votacoes[n].split(",")
		if int(voto[2]) == id_votacao:
			if voto[1] == "sim":
				contador_sim += 1
			else:
				contador_nao += 1
	resultado = [contador_sim,contador_nao]
	return resultado
		
