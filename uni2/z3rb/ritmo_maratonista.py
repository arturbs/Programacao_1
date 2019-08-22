# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  ritmo de um maratonista

percorrido = float(raw_input())
tempo = float(raw_input())

"""calculo"""
ritmo = tempo / percorrido

print ("O ritmo do maratonista foi %.2f min/km." %ritmo)
