# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Conversão de Matrículas na UFCG

matri_old = raw_input()
matri_new = "1"

for n in range(1,5):
	matri_new += matri_old[n]

matri_new += "0"

for n in range(5,len(matri_old)):
	matri_new += matri_old[n]
 
print matri_new
