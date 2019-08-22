# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  Nota na final

print ("== Estágio 1 ==")
peso1 = float(raw_input("Peso? "))
nota1 = float(raw_input("Nota? "))
print ("== Estágio 2 ==")
peso2 = float(raw_input("Peso? "))
nota2 = float(raw_input("Nota? "))
print ("== Estágio 3 ==")
peso3 = float(raw_input("Peso? "))
nota3 = float(raw_input("Nota? "))

"""calculos"""
media_parcial = ((peso1 * nota1) + (peso2 * nota2) + (peso3 * nota3)) / (peso1 + peso2 + peso3)
mediaf_5 = ((5.0 - media_parcial * 0.6)) / 0.4
mediaf_7 = ((7.0 - media_parcial * 0.6)) / 0.4

print ("== Resultados ==")
print ("Média parcial: %.1f" %media_parcial)
print ("Nota na final, pra média 5.0 = %.1f" %mediaf_5)
print ("Nota na final, pra média 7.0 = %.1f" %mediaf_7)

