# coding: utf-8
import math

velocidade_de_vazao = float(input())
diametro_cano = float(input())
seccao = (math.pi * diametro_cano**2) / 4
vazao = velocidade_de_vazao * seccao * 1000            #convertendo para litros
tempo = int(input())                                   #em segundos
quantidade_de_agua = tempo * vazao
print "Quantidade de água =", quantidade_de_agua, "litros."
