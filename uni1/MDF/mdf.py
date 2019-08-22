#coding: utf-8
nome = raw_input("Nome? ")
pletra = raw_input("Letra? R$ ")

quantidade = len(nome)
vfinal = quantidade * float(pletra)

print ("Orçamento: R$ " + str(vfinal))

