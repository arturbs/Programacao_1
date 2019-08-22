# coding: utf-8
# Calculando o consumo de energia em Joules

potencia = float(input())
tempo = float(input())

seg = tempo * 60            # conversão para segundos
consumoj = seg * potencia
consumokwh = consumoj/(1000*3600)

print str(consumokwh) + " kWh"    # resultado em Joules
