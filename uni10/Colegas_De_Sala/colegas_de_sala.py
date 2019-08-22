#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Agrupa negativos

def colegas_de_sala(salasprofs, professor):
    coleguinhas = []
    professores = salasprofs.keys()
    for n in professores:
        if salasprofs[professor] == salasprofs[n]:
            if professor != n:
                coleguinhas.append(n)
    return coleguinhas


