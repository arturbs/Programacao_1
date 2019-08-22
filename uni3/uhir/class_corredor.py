# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa : Classifica Corredor

kilometros = float(raw_input())
hora = float(raw_input())

velocidade = kilometros / hora

if velocidade < 10:
	print "Velocidade: %.1fkm/h. Corredor amador." %velocidade
elif velocidade <= 15:
	print "Velocidade: %.1fkm/h. Corredor aspirante." %velocidade
else:
	print "Velocidade: %.1fkm/h. Corredor profissional." %velocidade
