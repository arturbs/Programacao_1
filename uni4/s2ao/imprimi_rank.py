# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Imprime Ranking (Cumulativo)

posicao = 0
lista_de_times = ""
pontos_analizados = -1
times = int(raw_input())
contador = 0
verificador_de_igualdade = 0

for n in range(times):
	nome_time = raw_input()
	pontos_time = int(raw_input())
	
	if contador > 0:
		lista_de_times += "\n"
		
	if pontos_time > pontos_analizados:
		pontos_analizados = pontos_time
		posicao = n + 1
		contador += 1
		verificador_de_igualdade = 0
		lista_de_times += "%d. %s (%d)" %(posicao, nome_time, pontos_time)
		
	
		
	elif pontos_time == pontos_analizados:
		pontos_analizados = pontos_time
		contador += 1
		verificador_de_igualdade += 1
		posicao = n + 1 - verificador_de_igualdade
		lista_de_times += "%d. %s (%d)" %(posicao, nome_time, pontos_time)
		
		
		
	elif pontos_time < pontos_analizados:
		pontos_analizados = pontos_time
		posicao = n + 1
		contador += 1
		lista_de_times += "%d. %s (%d)" %(posicao, nome_time, pontos_time)
		verificador_de_igualdade = 0
		
		
		


	
print lista_de_times
