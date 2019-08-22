# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  tweets por pagina

tweets = int(raw_input())

paginas = tweets / 400
perdidos = tweets % 400
porcentagem = (float(perdidos) / tweets) * 100

print ("Serão necessárias %d página(s) para visualizar os tweets." %paginas)
print ("%.1f%% dos tweets serão perdidos." %abs(porcentagem))
