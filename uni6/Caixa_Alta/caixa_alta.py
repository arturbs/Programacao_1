#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#A Primeira Letra em Caixa Alta

def caixa_alta(frase):
	nova_frase = ""
	if len(frase) == 0:
		nova_frase == frase
	elif len(frase) == 1:
		nova_frase += frase.lower()
	else:
		if frase[1] != " ":
			nova_frase += frase[0].upper()
		else:
			nova_frase += frase[0].lower()
		for n in range(len(frase) - 2):
			if frase[n] == " ":
				if frase[n+2] != " ":
					nova_frase += frase[n+1].upper()
				elif frase[n+2] == " ":
					nova_frase += frase[n+1].lower()
				else:
					nova_frase += frase[n+1]
			else:
				nova_frase += frase[n+1]
		
		if frase[len(frase)-2] == " ":
			nova_frase += frase[len(frase)-1].lower()
		else:
			nova_frase += frase[len(frase)-1]
	
	print nova_frase
	return nova_frase

caixa_alta("A E i ou u")
