#coding: utf-8
#Mt_U10
#palavras na frase

def acha_palavras(frase):
    dicio = {}
    palavras = frase.split()
    for n in range(len(palavras)):
        if dicio.has_key(palavras[n]):
            dicio[palavras[n]].append(n)
        else:
            dicio[palavras[n]] = [n]
    return dicio




frase = 'caetano eh um aluno de computacao e artur eh um aluno de computacao'


print acha_palavras(frase)



'''caetano: 0
eh: 1 8
um: 2 9
aluno: 3 10
de: 4 11
computacao: 5 12
e: 6
artur: 7'''


'''numeros = [11, 15, 9, 150, 13, 0, 2, 10, 25]

fucçao(numeros, 3)
0:15 9 150 0
1:13 10 25
2:11 2'''