# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Descarta coincidente

quantidade = int(raw_input())
descarta = 0
descartados = ""
aceitos = ""
aceito = 0

for n in range(quantidade):
	numero = raw_input()
	for q in range(0,len(numero)):
		repeticoes = 0
		if int(numero[q]) == q and descarta > 0:
			descartados += "\n%s" %numero
			descarta += 1 
			repeticoes += 1
			break
		elif int(numero[q]) == q:
			descartados += numero
			descarta += 1 
			repeticoes += 1
			break
			
	if repeticoes == 0 and aceito > 0:
		aceitos +=  "\n%s" %numero
		aceito +=1
	elif repeticoes == 0:
		aceitos += numero 
		aceito +=1
		

print "---"
print "%d aceito(s)" %aceito 
if aceito > 0:
	print aceitos 
print "%d descartado(s)" %descarta
if descarta > 0:
	print descartados 



