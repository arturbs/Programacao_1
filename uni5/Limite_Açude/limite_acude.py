#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamação 1, 2018.2
#Limite açude

limite_superior = float(raw_input())
nivel_atual = float(raw_input())

while nivel_atual < limite_superior:
	eventos = raw_input()
	eventos.split()
	tipo, quantidade = eventos.split()
	if tipo == "chuva":
		nivel_atual += float(quantidade)
	elif tipo == "afluente":
		nivel_atual += float(quantidade)
	elif tipo == "demanda":
		if nivel_atual - float(quantidade) < 0:
			nivel_atual = nivel_atual
		elif nivel_atual - float(quantidade) >= 0:
			nivel_atual -= float(quantidade)
			
print "Açude passou a liberar água."
print "Nível: %.2f" %nivel_atual

