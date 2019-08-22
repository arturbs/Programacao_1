# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 10/09/2018 
# Programa : iptu

""" dados colocados pelo usuário """
area = float(raw_input("Área construída? "))
aliquota = float(raw_input("Alíquota? "))

"""cálculo do IPTU e de suas versões de pagamento """
iptu = (area * aliquota) + 35.0
parcela1 = iptu * 0.75
parcela6 = iptu * 0.95
cadaParcela6 = parcela6 / 6
cadaparcela10 = iptu / 10

"""prints das informações"""
print ("IPTU: R$ %.2f" %iptu)
print ("")
print ("Pagamento:")
print ("1. Quota única. R$ %.2f" %parcela1)
print ("2. Em 6 parcelas. Total: R$ %.2f" %parcela6)
print ("   6 x R$ %.2f" %cadaParcela6)
print ("3. Em 10 parcelas. Total: R$ %.2f" %iptu)
print ("   10 x R$ %.2f" %cadaparcela10)
