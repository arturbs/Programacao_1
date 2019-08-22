# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 10/09/2018 
# Programa : mega tripla

"""dados fornecidos pelo usuario"""
num1 = int(raw_input())
num2 = int(raw_input())
num3 = int(raw_input())

"""divisões dos numeros para eles serem numero possiveis"""
num1 = num1 % 11
num2 = num2 % 11
num3 = num3 % 11

print ("%.2d-%.2d-%.2d" %(int(num1), int(num2), int(num3)))
