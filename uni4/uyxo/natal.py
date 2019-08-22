#coding:utf-8
#Artur Brito Souza - 118210056
#Programação 1 - 17/09/2018
#Arvore de natal

altura = int(raw_input())
alt = altura
centro = 1
for n in range(0,altura):
	print" " * (alt - 1) + "o" * centro
	alt -= 1
	centro += 2
print " " * (altura -1) + "o"
