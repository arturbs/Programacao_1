#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Agenda Telefônica

lista= []
def lista_telefonica(operacao):
	if operacao == "inserir":
		quantidade = raw_input()
		for n in range(int(quantidade)):
			lista.append(raw_input())
			lista.append(raw_input())
	for w in range(0, len(lista) - 2, 2):
		if lista[w] > lista[w + 2]:
			lista[w], lista[w+2] = lista[w+2], lista[w]
			lista[w+1], lista[w+3] = lista[w+3], lista[w+1]
			
		
	
	if operacao == "buscar":
		contador = 0
		palavra_a_buscar = raw_input()
		for l in range(0,len(lista),2):
			if str(lista[l]) == str(palavra_a_buscar):
				print "Nome: %s" %lista[l]
				print "Fone: %s" %lista[(l+1)]
				print "----------"
				contador += 1
		if contador == 0:
			print "Nome inexistente"
			print "----------"   
	
	if operacao == "imprimir":
		for q in range(0, len(lista), 2):
			print "Nome: %s" %lista[q]
			print "Fone: %s" %lista[(q+1)]
			print "----------"
			
		
		
		
operacao = ""
while operacao != "finalizar":
	operacao = raw_input()
	lista_telefonica(operacao)


