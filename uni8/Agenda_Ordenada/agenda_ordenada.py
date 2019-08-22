#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Agenda Ordenada

def ordena(nomes, ultimo):
    for n in range(len(nomes)):
        for i in range(len(nomes)-1):
            if nomes[i] > nomes[i+1]:
                nomes[i], nomes[i+1] = nomes[i+1], nomes[i]
    for l in nomes:
        if l == ultimo:
            print "* %s" %l
        else:
            print l
    print "----"



nomes = []
entrada = ""
while entrada != "####":
    entrada = raw_input()
    if entrada != "####":
        nomes.append(entrada)
        ordena(nomes, entrada)
