#coding:utf-8
#Artur Brito Souza - 118210056
#Programação 1 - 17/09/2018
#Aprovados e Reprovados

alunos = int(raw_input())
aprovados = 0
reprovados = 0
alunos_aprovados = 0
alunos_reprovados = 0
n = 0

for n in range(0,alunos):
	nota = float(raw_input())
	if nota >= 7.0:
		aprovados += nota
		alunos_aprovados += 1
	else:
		reprovados += nota
		alunos_reprovados += 1

print "Reprovados: %d" %alunos_reprovados
if alunos_reprovados > 0:
	media_reprovados = reprovados / alunos_reprovados
	print "Média: %.1f" %media_reprovados

print ""

print "Aprovados: %d" %alunos_aprovados
if alunos_aprovados > 0:
	media_aprovados = aprovados / alunos_aprovados
	print "Média: %.1f" %media_aprovados
		
