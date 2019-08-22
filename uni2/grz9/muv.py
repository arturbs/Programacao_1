# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 10/09/2018 
# Programa :  MRV

"""DADOS INSERIDOS PELO USUÁRIO"""
pos_ini = float(raw_input("Posição inicial? "))
vel_ini = float(raw_input("Velocidade inicial? "))
tempo = float(raw_input("Tempo? "))
acel = float(raw_input("Aceleração? "))

"""calculos do MUV"""
vel_fin = vel_ini + (acel * tempo)
pos_fin = pos_ini + (vel_ini * tempo) + ((acel * (tempo * tempo)) / 2)
vel_media = (pos_fin - pos_ini) / tempo

"""prints determinados pela questão"""
print ("")
print ("Dados da questão")
print ("================")
print ("   Posição inicial: %.2f m" %pos_ini)
print ("Velocidade inicial: %.2f m/s" %vel_ini)
print ("        Aceleração: %.2f m/s2" %acel)
print ("             Tempo: %.2f s" %tempo)
print ("  Velocidade final: %.2f m/s" %vel_fin)
print ("  Velocidade média: %.2f m/s" %vel_media)
print ("     Posição final: %.2f m" %pos_fin)
