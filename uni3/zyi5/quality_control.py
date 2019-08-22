# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Controle de Qualidade

peso_congelado = float(raw_input())
peso_descongelado = float(raw_input())

peso_agua = peso_congelado - peso_descongelado 
porcentagem = (peso_agua / peso_congelado) * 100

print "%.1f%% do peso do produto é de água congelada." %porcentagem
if porcentagem < 5:
	print "Produto qualis A."
elif porcentagem < 10:
	print "Produto em conformidade."
else:
	print "Produto não conforme."
