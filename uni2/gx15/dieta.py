# coding: utf-8

qPerder = float(input())
tExercicios = float(input())
qCalorias = float(input())

dias = (qPerder * 7700) / (( tExercicios * 900) + (2000 - qCalorias))


print ("Você precisará de %.2f dias de dieta" %dias)
