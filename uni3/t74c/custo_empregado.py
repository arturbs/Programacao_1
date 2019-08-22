# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# Programa :  Custo Empregado

salario_base = float(raw_input())
dias_trabalhados = int(raw_input())
transporte_diario = float(raw_input())

fgts = (salario_base / 100) * 8
inss_empregador = (salario_base / 100) * 12
preco_transporte = dias_trabalhados * transporte_diario

se_transporte_for_caro = 0
if preco_transporte <= ((salario_base / 100) * 6):
	transporte = 0
else:
	transporte = (salario_base / 100) * 6
	se_transporte_for_caro = preco_transporte - transporte
	
if salario_base <= 1317.07:
	inss_empregado = (salario_base / 100.0) * 8
elif salario_base <= 2195.12:
	inss_empregado = (salario_base / 100.0) * 9
else:
	inss_empregado = (salario_base / 100.0) * 11
	
salario_liquido = salario_base - inss_empregado - transporte
custo_do_empregador = salario_base + inss_empregador + fgts + se_transporte_for_caro


print "O salário base é R$ %.2f" %salario_base
print "O custo mensal para o empregador é de R$ %.2f" %custo_do_empregador
print "O salário líquido que o trabalhador irá receber no mês é R$ %.2f" %salario_liquido
