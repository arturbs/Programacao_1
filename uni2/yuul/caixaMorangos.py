#coding: utf-8
morangos = int(input())

caixas = morangos / 400
desperdicio = morangos % 400
porcentagem = (float(desperdicio) / morangos) * 100

print("Serão necessárias %d caixa(s) para embalar os morangos." %caixas)
print("%.1f%% dos morangos serão perdidos." %porcentagem)

