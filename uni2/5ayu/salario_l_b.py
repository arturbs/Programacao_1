# coding: utf-8
# aluno: Artur Brito Souza
# matricula: 118210056
# UFCG - Programação 1 2018.2
# 12/09/2018 
# Programa :  salario liquido e bruto

"""entrada das variaveis pelo usuario"""
nome = raw_input()
hora_extra = float(raw_input())
salario_min = float(raw_input())
valor_hora_extra = float(raw_input())

"""calculos"""
pagamento_hora_extra = hora_extra * valor_hora_extra
salario_bruto = (4 * salario_min) + pagamento_hora_extra
desconto_inss = 0.12 * salario_bruto
desconto_imposto_renda = 0.2 * salario_bruto
salario_liquido = salario_bruto - (desconto_imposto_renda + desconto_inss)

"""prints das informaçoes como a questão pede"""
print ("O Salário Bruto de %s é de R$ %.2f" %(nome, salario_bruto))
print ("O Salário Líquido de %s é de R$ %.2f" %(nome, salario_liquido))
