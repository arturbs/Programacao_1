#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamação 1, 2018.2
#Calculadora

controle = 0

while controle != 5:
	entrada = raw_input()
	if entrada ==  "5":
		controle = 5
	else:
		entrada.split()
		operacao,num1, num2 = entrada.split()
		controle = int(operacao)
	
	def soma(num1, num2):
		resultado = int(num1) + int(num2)
		print resultado
	def subtracao(num1, num2):
		resultado = int(num1) - int(num2)
		print resultado
	def multiplicacao(num1, num2):
		resultado = int(num1) * int(num2)
		print resultado
	def divisao(num1, num2):
		if int(num2) ==  0:
			print "Erro: Divisão por 0"
		else:
			resultado = int(num1) / int(num2)
			print resultado

	if controle == 1:
		soma(num1,num2)
	elif controle == 2:
		subtracao(num1, num2)
	elif controle == 3:
		multiplicacao(num1, num2)
	elif controle == 4:
		divisao(num1, num2)



