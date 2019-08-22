# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Ciclo Trig.


angulo = int(raw_input())
angulo = angulo % 360

if angulo == 0:
	print "Sobre eixos"
elif angulo < 90:
	print "Quadrante 1"
elif angulo == 90:
	print "Sobre eixos"
elif angulo < 180:
	print "Quadrante 2"
elif angulo == 180:
	print "Sobre eixos"
elif angulo < 270:
	print "Quadrante 3"
elif angulo == 270:
	print "Sobre eixos"
elif angulo < 360:
	print "Quadrante 4"
else:
	print "Sobre eixos"
