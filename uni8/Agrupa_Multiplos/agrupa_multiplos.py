#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Agrupa Múltiplos

def agrupa_multiplos(seq, k):
	for n in range(len(seq)-1, -1, -1):
		if seq[n] % k == 0:
			seq[n], seq[n-1] = seq[n-1], seq[n]
	
	print seq

seq = [6, 15, 12, 6, 8, 3, 25, 14, 1, 10, 7]
agrupa_multiplos(seq, 5)
			
			
	
	










