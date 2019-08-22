#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Disciplinas de um Professor

def disciplinas(alocacao, professor):
	creditos = 0
	disciplinas = []
	tamanho = alocacao.keys()
	for n in range(len(tamanho)):
		for j in alocacao[tamanho[n]]:
			if j == professor:
				disciplinas.append(tamanho[n][0])
				creditos += int(tamanho[n][1])
	return disciplinas, creditos
     
		
	
	
	
alocacao = {("P1", 4): ['Jorge', 'Dalton','Wilkerson'],
         ("LP1", 4): ['Jorge', 'Dalton', 'Eliane', 'Wilkerson'],
         ("EVOL", 2): ['Dalton'],
         ("IC", 4): ['Eliane', 'Joseana'],
         ("P2", 4): ['Livia', 'Raquel', 'Nazareno'],
         ("GRAFOS", 2): ['Patricia', 'Patricia']}

print disciplinas(alocacao,"Dalton")
'''
assert set(disciplinas(alocacao, "Dalton")[0]) == set(['P1', 'LP1', 'EVOL'])
assert disciplinas(alocacao, "Dalton")[1] == 10
assert set(disciplinas(alocacao, "Eliane")[0]) == set(['LP1', 'IC'])
assert disciplinas(alocacao, "Eliane")[1] == 8
assert set(disciplinas(alocacao, "Patricia")[0]) == set(['GRAFOS'])
assert disciplinas(alocacao, "Patricia")[1] == 4
'''
