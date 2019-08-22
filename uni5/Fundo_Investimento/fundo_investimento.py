#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamação 1, 2018.2
#Fundo de Investimento


contador = 0
fundo_de_investimento = 0
media = 0
controle = True
while controle:
	contribuicoes = float(raw_input())
	if contribuicoes < media:
		controle = False
	else:
		contador += 1
		fundo_de_investimento += contribuicoes
		media = fundo_de_investimento / contador

print "Saldo total do FIS: R$%.2f." %fundo_de_investimento
print "Média das contribuições: R$%.2f." %media
