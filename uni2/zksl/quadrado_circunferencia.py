# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  perimetro triangulos
import math

lado = float(raw_input())

"""calculando perimetro e area ( como o lado vai ser o diametro da circuferencia)"""
diagonal = math.sqrt((lado ** 2) * 2)
raio = diagonal / 2
area = math.pi * raio ** 2
perimetro = 2 * math.pi * raio




"""printando o nescessario"""
print ("Perímetro: %.5f" %perimetro)
print ("Área: %.5f" %area)
