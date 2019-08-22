safra = float(input())
atacado = int(input())
varejo = int(input())

pAtacado = safra / atacado
sobra = safra % atacado
pVarejo = sobra / varejo 


print ("Clientes no atacado = %dkg cada." %int(pAtacado)) 
print ("Clientes no varejo = %.2fkg cada." %pVarejo)
