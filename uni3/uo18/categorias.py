# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  categoria

nome = raw_input()
idade = int(raw_input())

if idade < 5:
	print "%s, %d anos, Não pode competir." %(nome,idade)
elif idade <= 7:
	print "%s, %d anos, Infantil A." %(nome,idade)
elif idade <= 10:
	print "%s, %d anos, Infantil B." %(nome,idade)
elif idade <= 13:
	print "%s, %d anos, Juvenil A." %(nome,idade)
elif idade <= 17:
	print "%s, %d anos, Juvenil B." %(nome,idade)
elif idade > 17:
	print "%s, %d anos, Senior." %(nome,idade)
