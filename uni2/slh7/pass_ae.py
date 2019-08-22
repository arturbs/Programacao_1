# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa : Passagem aérea

"""recebimento da  variável"""
distancia = float(raw_input())
aliquota = float(raw_input())

"""contas"""
passagem = 51 + (distancia * aliquota)
a_vista = passagem * 0.75
em_6_parcelas = passagem * 0.95
cada_6 = em_6_parcelas / 6.0
em_10_parcelas = passagem 
cada_10 = em_10_parcelas / 10.0

print ("Valor da passagem: R$ %.2f\n" %passagem)
print ("Pagamento:")
print ("1. À vista. R$ %.2f" %a_vista)
print ("2. Em 6 parcelas. Total: R$ %.2f" %em_6_parcelas)
print ("   6 x R$ %.2f" %cada_6)
print ("3. Em 10 parcelas. Total: R$ %.2f" %em_10_parcelas)
print ("   10 x R$ %.2f" %cada_10)





