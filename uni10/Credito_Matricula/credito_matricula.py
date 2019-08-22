#coding:utf-8
#Artur Brito Souza - 118210056
#Laboratorio de Progamacao 1, 2018.2
#Crédito Matrícula

def num_creditos(bd_ufcg, matricula):
    tamanho = bd_ufcg.keys()
    creditos = 0
    for n in range(len(tamanho)):
        tamanho2 = bd_ufcg[tamanho[n]].keys()
        for l in range(len(tamanho2)):
            for j in bd_ufcg[tamanho[n]][tamanho2[l]]:
                if j == matricula:
                    creditos += int(tamanho2[l][1])
    return creditos
	
	
bd_ufcg = {"UASC": {("Programação I", 4): ["11624100", "11624400"], ("Programação II", 4): ["11624200"], ("Teoria dos Grafos", 2): ["11624200"]},
           "UAF": {("Física Clássica", 4): ["11624200"], ("Física Moderna", 4): ["11624300", "11624500", "11624600"]},
           "UAM": {("Cálculo I", 4): ["11624100", "11624300"], ("Álgebra Linear", 4): ["11624300"]}
           }

print num_creditos(bd_ufcg, "11624100") 
	
	
	
	

