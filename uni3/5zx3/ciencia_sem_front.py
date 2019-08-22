# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa : Ciência sem Fronteiras

enem = int(raw_input())
creditos = float(raw_input())
porcentagem = (creditos / 416) * 100

if enem < 600 and (porcentagem < 20 or porcentagem > 90):
	print "Nenhuma condição satisfeita."
elif enem < 600:
	print "Condição ENEM não satisfeita."
elif porcentagem < 20 or porcentagem > 90:
	print "Condição CRÉDITOS não satisfeita."
else:
	print "Todas as condições satisfeitas."


