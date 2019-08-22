# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  perimetro triangulos
import math

"""dados inseridos pelo usuario"""
x1 = int(raw_input())
y1 = int(raw_input())
x2 = int(raw_input())
y2 = int(raw_input())
x3 = int(raw_input())
y3 = int(raw_input())

"""calculo dos lados e perimetro"""
lado1 = math.sqrt(((x1 - x2) ** 2) + ((y1 - y2)**2))
lado2 = math.sqrt(((x2 - x3) ** 2) + ((y2 - y3)**2))
lado3 = math.sqrt(((x3 - x1) ** 2) + ((y3 - y1)**2))
perimetro = lado1 + lado2 + lado3

print ("O perímetro é de %.2f" %abs(perimetro))
