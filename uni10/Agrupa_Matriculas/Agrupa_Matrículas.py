#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Agrupa Múltiplos

def agrupa_por_periodo(alunos):
    periodo = {}
    aux = []
    aux2 = []
    cont = 0
    aux.append(str(alunos[0][0:3]))

    for n in range(len(alunos)):
        for i in aux:
            if alunos[n][0:3] == i:
                cont += 1
        if cont == 0:
            aux.append(str(alunos[n][0:3]))
        cont = 0

    for k in aux:
        for j in range(len(alunos)):
            if alunos[j][0:3] == k:
                cont+=1
        aux2.append(cont)
        cont = 0

    for l in range(len(aux)):
        periodo.update({aux[l] : aux2[l]})
    return periodo