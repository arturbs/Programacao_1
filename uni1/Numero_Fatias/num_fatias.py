#coding: utf-8
#artur brito souza - 118210056
#UFCG - Programação 1
#Número de Fatias

convidados = float(raw_input())
op1_inteira = 32 / convidados
op1_resto  = 32 % convidados
op2 = 32 / convidados

print 'Opção 1: %d fatias cada, %d de resto' %(op1_inteira,op1_resto)
print 'Opção 2: %.2f fatias cada' %op2
