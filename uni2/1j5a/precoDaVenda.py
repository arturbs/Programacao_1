# coding: utf-8

cEntrada = float(input())
pDespesas = float(input())
pLucro = float(input())
pImposto = float(input())
pComissao = float(input())
pDesconto = float(input())
pEncargo = float(input())

valor_final1 = ((cEntrada + ((cEntrada / 100) * pDespesas) + ((cEntrada / 100) * pLucro)) * 100) 
valor_final2 = (100 - pImposto - pComissao - pDesconto - pEncargo)
valor_final3 = valor_final1 / valor_final2 
real = int(valor_final3)
moeda = valor_final3 - int(valor_final3)

print ("Preço de venda é R$ %.2f (R$ %.2f + R$ %.2f)" %(valor_final3, float(real), moeda))
