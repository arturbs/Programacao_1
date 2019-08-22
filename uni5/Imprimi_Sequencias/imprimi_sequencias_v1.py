#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamação 1, 2018.2
#Imprime Sequencias de Números Inteiros

numero_alvo = float(raw_input())
sequencia = "" 
conjunto_de_sequencias = []

while sequencia != "fim":
	sequencia = raw_input()
	conjunto_de_sequencias.append(sequencia.split())

sequencia_certa = ""
contador = 0
for n in range(len(conjunto_de_sequencias) - 1):
	contador = 0
	for i in range(len(conjunto_de_sequencias[n])):
		if float(conjunto_de_sequencias [n][i]) >= numero_alvo:
			contador += 1
	if contador >= len(conjunto_de_sequencias[n])/2.0 :
		for i in range(len(conjunto_de_sequencias[n])):
			sequencia_certa += " " + str(conjunto_de_sequencias[n][i])
		print "sequencia %d:%s" %(n + 1,sequencia_certa )
		sequencia_certa = ""
