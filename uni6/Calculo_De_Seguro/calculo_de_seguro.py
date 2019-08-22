#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#A Primeira Letra em Caixa Alta

def calcula_seguro(valor_veiculo, lista):
	idade = lista[0]
	relacionamento = lista[1]
	moradia_risco = lista[2]
	portao = lista[3]
	casa = lista[4]
	casa_propria = lista[5]
	uso = lista[6]
	pontos = 0
	if idade < 22:
		pontos += 20
	elif idade < 31:
		pontos += 15
	elif idade < 41:
		pontos += 12
	elif idade < 61:
		pontos += 10
	else:
		pontos += 20
		
	if relacionamento == True:
		pontos += 10
	else:
		pontos += 20
		
	if moradia_risco == True:
		pontos += 20
	else:
		pontos += 10
		
	if portao == True:
		pontos += 20
	else:
		pontos += 10
		
	if casa == True:
		pontos += 20
	else:
		pontos += 10
		
	if casa_propria == True:
		pontos += 10
	else:
		pontos += 20
		
	if uso == "Trabalho":
		pontos += 10
	else:
		pontos += 20
		
	if pontos <= 80:
		risco = "Risco Baixo"
		pago_ao_seguro = (valor_veiculo / 100.0) * 10
	elif pontos <= 100:
		risco = "Risco Medio"
		pago_ao_seguro = (valor_veiculo / 100.0) * 20
	else:
		risco = "Risco Alto"
		pago_ao_seguro = (valor_veiculo / 100.0) * 30
		
	return [pontos, risco, pago_ao_seguro]









