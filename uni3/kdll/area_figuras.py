# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 14/09/2018 
# Programa :  area figuras
import math

figura = raw_input()

if figura == "triângulo":
	base = float(raw_input())
	altura = float(raw_input())
	area_trian = (base * altura) / 2
	print "Área do triângulo: %.2f (cm2)" %area_trian
elif figura == "retângulo":
	base = float(raw_input())
	altura = float(raw_input())
	area_retan = (base * altura) 
	print "Área do retângulo: %.2f (cm2)" %area_retan
elif figura == "círculo":
	raio = float(raw_input())
	area_circ = (raio ** 2) * math.pi
	print "Área do círculo: %.2f (cm2)" %area_circ
elif figura == "quadrado":
	lado = float(raw_input())
	area_quad = lado ** 2
	print "Área do quadrado: %.2f (cm2)" %area_quad
	
