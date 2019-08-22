# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  novo CPF

"""recebimento da  variável"""
parte1 = raw_input()
parte2 = raw_input()
parte3 = raw_input()

"""calculo da parte 4 do CPF"""
parte4 = (int(parte3[0]) + int(parte3[1]) + int(parte3[2]))

print ("%s.%s.%s-%.2d" %(parte1, parte2, parte3, int(parte4)))
