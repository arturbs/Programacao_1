#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Acima da média (Criminalidade)

entrada = 0
cont = 0
valores = []
total = 0
teste = 0
total_teste = 0

media_ssp = float(raw_input())

while entrada != "fim": #Esse while serve para receber os valores
	entrada = raw_input()
	if entrada != "fim":
		valores.append(entrada)
		cont += 1
		linha_teste = valores[cont-1].split(" ")
		for j in range(len(linha_teste)):
			total_teste += float(linha_teste[j])
		media_teste = total_teste/(j+1)
		total_teste = 0
		if media_teste < media_ssp/2:
			entrada = "fim"

media = range(len(valores))

for n in range(len(valores)):	#Esse for calcula a media de cada entrada
	linha = valores[n].split(" ")
	for i in range(len(linha)):
		total += float(linha[i])
	media[n] = total/(i+1)
	total = 0

while teste < cont:
	if media[teste] > media_ssp:
		print valores[teste]
	teste += 1
