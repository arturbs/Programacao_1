#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Agrupa negativos

def agrupa_negativos(lista):
    negativo = []
    positivo = []
    for n in range(len(lista)):
        if lista[n] < 0:
            negativo.append(lista[n])
        else:
            positivo.append(lista[n])
    nao_negativos = {"nao-negativos":positivo}
    negativos = {"negativos": negativo}
    negativos.update(nao_negativos)
    return negativos

lista = [-7, 8, -11, 15, 18]
print agrupa_negativos(lista)