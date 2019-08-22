# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  tinta

"""entrada das variaveis pelo usuario"""
altura = float(raw_input())
largura = float(raw_input())

"""calculos"""
area_parede = altura * largura
tinta = area_parede / 13.8888888888 

print ("%.2f l" %tinta)
