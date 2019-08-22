# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  Nota na final
import math

"""entrada de dados"""
raio = float(raw_input())

"""calculando a area ( como o lado vai ser o diametro da circuferencia)"""
area_circuf = math.pi * raio ** 2
diagonalq = raio * 2
ladoq = math.sqrt((diagonalq ** 2) / 2)
area_quadra = ladoq * ladoq
area_incomum = area_circuf - area_quadra

print ("Área não comum: %.5f" %area_incomum)



