#FFFFFF# coding: utf-8
# Eleição na ADUF

abstencao = float(raw_input())
a_favor = float(raw_input())
contra = float(raw_input())
total = abstencao + a_favor + contra

porc_abst = (abstencao / total) * 100
porc_afav = (a_favor / total) * 100
porc_cont = (contra / total) * 100

print "Resultado da Votação"
print
print ("%d abstenções (%.2f%%)" %(abstencao, porc_abst))
print ("%d a favor (%.2f%%)" %(a_favor, porc_afav))  
print ("%d contra (%.2f%%)" %(contra, porc_cont))  
