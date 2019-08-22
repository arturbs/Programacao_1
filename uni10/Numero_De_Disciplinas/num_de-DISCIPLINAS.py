#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Número de Disciplinas

def  numero_disciplinas(grade,horarios, cad_pagas):
	requisitos = []
	contador = 0
	paga = 0
	for n in grade:
		paga = 0
		for q in range(len(cad_pagas)):
			if cad_pagas[q] == n:
				paga +=1
	if paga == 0:
		contador += 1
	return contador
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
grade = {"p1": [], "lp1": [], "ic": [],"calc1": [], "p2": ["ic", "p1", "lp1"],
"lp2": ["ic", "p1", "lp1"], "grafos": ["ic", "p1", "lp1"], "calc2"  : ["calc1"], 
"edados": ["ic", "p1", "lp1", "p2", "lp2", "grafos"],
"leda": ["ic", "p1", "lp1", "p2", "lp2", "grafos"]}

horarios= {"p1": "s082", "lp1": "x082", "ic": "i142", "calc1": "q082", "p2": "t162",
"lp2": "s082", "grafos": "q082", "calc2": "x162", "edados": "x162", "leda": "t102"}

print numero_disciplinas(grade, horarios, [])
print numero_disciplinas(grade, horarios, ["ic", "p1", "lp1"])

