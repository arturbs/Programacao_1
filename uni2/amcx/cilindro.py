#coding: utf-8
import math

'''$ python supcilindro.py'''
print("Cálculo da Superfície de um Cilindro")
print ("---")

diametro = float(raw_input("Medida do diâmetro? ")) 
altura = float(raw_input("Medida da altura? ")) 

raio = diametro / 2
area_base = math.pi * (raio ** 2)
area_lateral = 2 * math.pi * raio * altura
area_total = 2 * area_base + area_lateral

print ("---")
print ("Área calculada: %.2f" %area_total)
