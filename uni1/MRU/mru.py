# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 10/09/2018 

'''variaveis dadas pelo usuario '''
posicaoInicial = float(input())
velocidade = float(input())
tempoDesejado = float(input())

'''calculo'''
posicaoFinal = posicaoInicial + (velocidade * tempoDesejado)

print ("Posição final do móvel")
print ("S(%.1f) = %.1f m" %(tempoDesejado, posicaoFinal))
