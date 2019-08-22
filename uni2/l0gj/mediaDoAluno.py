# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 10/09/2018 
# Programa : media do aluno

"""dados das notas que o usuário coloca"""
nota1 = float(raw_input())
nota2 = float(raw_input())
nota3 = float(raw_input())

"""calculo da nota final de acordo com o cálculo pedido"""
notaFinal = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

"""print da nota final"""
print notaFinal
