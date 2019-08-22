# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa : Índices de caracteres


palavra_para_inspecionar = raw_input()
caracteres_desejados = raw_input()

lista_ordem = ""
contador = 0
for q in range(len(caracteres_desejados) ):
	
	for n in range(len(palavra_para_inspecionar) ):
		if caracteres_desejados[q] == palavra_para_inspecionar[n]:
			lista_ordem += "%d" %n
		elif  caracteres_desejados[q] == palavra_para_inspecionar[n] and contador > 0:
			lista_ordem += " " + "%d" %n
		else:
			lista_ordem = "-1"
		
		print lista_ordem
