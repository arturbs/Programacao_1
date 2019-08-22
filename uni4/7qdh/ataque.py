#coding:utf-8
#Artur Brito Souza - 118210056
#Programação 1 - 17/09/2018
#Ataque Mais Positivo de um Campeonato

times = int(raw_input())
gols = 0
time = "vazio"
gols_totais = 0

for n in range(times):
	time1 = raw_input()
	gols1 = int(raw_input())
	gols_totais += gols1
	if gols1 > gols:
		time = time1
		gols = gols1
	elif gols1 == gols:
		time = time + "\n" + time1
media = float(gols_totais) / times
print "Time(s) com melhor ataque (%d gol(s)):" %gols
print time
print "\nMédia de gols marcados: %.1f" %media
