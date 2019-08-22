# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa : resumo das vendas

brinquedos_total = int(raw_input())
teresa = int(raw_input())
carla = int(raw_input())

joaquim = brinquedos_total - teresa - carla
p_teresa = (float(teresa) / brinquedos_total) * 100
p_carla = (float(carla) / brinquedos_total) * 100
p_joaquim = (float(joaquim) / brinquedos_total) * 100

print ("Teresa vendeu %d (de %d) brinquedos. (%.2f%%)" %(teresa, brinquedos_total, p_teresa))
print ("Joaquim vendeu %d (de %d) brinquedos. (%.2f%%)" %(joaquim, brinquedos_total, p_joaquim))
print ("Carla vendeu %d (de %d) brinquedos. (%.2f%%)" %(carla, brinquedos_total, p_carla))
