# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 14/09/2018 
# Programa :  Avaliação de Desempenho Acadêmico

semestres = int(raw_input())
p_atividade_ensino = int(raw_input())
p_producao_intelectual = int(raw_input())
p_atividade_orientacao = int(raw_input())
p_atividade_administrativa = int(raw_input())

media = (p_atividade_ensino + p_producao_intelectual + p_atividade_orientacao + p_atividade_administrativa) / semestres

if semestres < 4:
	print "Promoção indeferida. Número de semestres insuficiente."
elif p_atividade_ensino < 320:
	print "Promoção indeferida. Pontuação mínima não alcançada."
elif p_producao_intelectual < 100:
	print "Promoção indeferida. Pontuação mínima não alcançada."
elif p_atividade_orientacao < 20:
	print "Promoção indeferida. Pontuação mínima não alcançada."
elif media < 140:
	print  "Promoção indeferida. Média insuficiente." 
else: 
	print "Promoção deferida. Parabéns!"
