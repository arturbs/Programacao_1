#coding: utf-8

capacidade = float(raw_input ("capacidade? "))
porcentagem = float(raw_input ("percentual hoje? "))
consumo_diario = float(raw_input ("gasto diário? "))

volume = capacidade * (porcentagem/100) 
dresto = volume / consumo_diario

print ("volume: %.2f" %volume)
print ("dias restantes: %d" %dresto)



