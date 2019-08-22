# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  reajuste salario minimo


salario_atual = float(raw_input("Valor atual? "))
salario_alterado =float(raw_input("Novo valor? "))

reajuste = ((salario_alterado - salario_atual) / salario_atual) * 100  


print ("Reajuste de %.1f%%" %reajuste)
