#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Inverte Dicionário

def  inverte_dicionario(dicionario):
	dic_inv = {}
	for n in range(len(dicionario)):
		if dic_inv.has_key(dicionario.values()[n]):
			dic_inv[dicionario.values()[n]].append(dicionario.keys()[n])
		else:
			dic_inv[dicionario.values()[n]] = [dicionario.keys()[n]]
	for q in dic_inv.values():
		for i in range(len(q)):
			for j in range(len(q)-1):
				if q[j] >= q[j+1]:
					q[j],q[j+1]=q[j+1],q[j]
	return dic_inv

m = {"a": 2, "b": 3, "c": 2}

print inverte_dicionario(m)



