import math

cateto1 = raw_input("Medida do Cateto 1? ")
cateto2 = raw_input("Medida do Cateto 2? ")

hipotenusa = math.sqrt((float(cateto1) ** 2 + float(cateto2) ** 2))

print ("Medida da Hipotenusa: %.2f" %hipotenusa )
