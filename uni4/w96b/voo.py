#coding:utf-8
#Artur Brito Souza - 118210056
#Programação 1 - 17/09/2018
#Autorização voos

tempo_disponivel = int(raw_input())
voos = int(raw_input())
autorizados = 0

for n in range(voos):
	tempo_voo = int(raw_input())
	if tempo_voo <= tempo_disponivel:
		tempo_disponivel -= tempo_voo
		autorizados += 1
		
print "%d voo(s) autorizados." %autorizados
