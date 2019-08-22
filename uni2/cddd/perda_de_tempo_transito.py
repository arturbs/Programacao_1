# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  lost of time in traffic

"""recebimento das variaveis"""
dia1 = int(raw_input())
dia2 = int(raw_input())
dia3 = int(raw_input())
dia4 = int(raw_input())
dia5 = int(raw_input())

"""calculo do programa"""
total_dias = dia1 + dia2 + dia3 + dia4 + dia5
media = total_dias / 5.0
porcentagem = (total_dias / 7200.0) * 100
episodios = total_dias / 50.0

print ("Você perdeu %d min na semana (média de %.1f min por dia)." %(total_dias,media))
print ("Isso significa %.2f%% da sua semana produtiva." %porcentagem)
print ("Daria para assistir %d episódio(s) de House." %int(episodios))
