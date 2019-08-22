fahr = float(input())

cels = (fahr - 32) * (5.0/9)
kel = cels + 273.15

print ("Fahrenheit: %0.3f F" %fahr)
print ("Celsius: %0.3f C" %cels)
print ("Kelvin: %0.3f K" %kel)
