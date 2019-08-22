#coding: utf-8
#artur brito souza - 118210056
#UFCG - Programação 1
#Grep

palavra_chave = raw_input()
num_frases = int(raw_input())

for n in range(num_frases):
	frase = raw_input()
	m = 0
	for q in range(len(frase)):
		if len(frase) > q + 2:
			if palavra_chave[m] == frase[q]:
				if palavra_chave[m+1] == frase [q+1]:
					if palavra_chave[m+2] == frase[q+2]:
						print frase
