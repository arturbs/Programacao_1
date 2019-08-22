# coding: utf-8

volume_caixa = float(raw_input("Capacidade de revestimento?"))

print(" ")
print ("== Dados do vão a revestir ==")

comprimento = float(raw_input("Comprimento? "))
largura = float(raw_input("Largura? "))
altura = float(raw_input("Altura?"))

area_total = (comprimento * altura * 2) + ( comprimento * largura) + ( largura * altura * 2)
numero_caixas = area_total / volume_caixa

print (" ")
print("== Resultados ==")
print ("Área total a revestir: %.1f m2" %area_total)
print ("Número de caixas: %d" %int(numero_caixas))
