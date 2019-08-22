# coding: utf-8

unidade = raw_input('Unidade? ')
media = raw_input('Média de aprovação na unidade? ')

proxima_unidade = int(unidade) + 1
msg = 'O aluno vai para a unidade %d com média %.1f.' %(proxima_unidade, float(media))

print ("")
print msg 
