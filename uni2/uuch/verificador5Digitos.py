conta = raw_input()

a = conta [0]
b = conta [1]
c = conta [2]
d = conta [3]
e = conta [4]

verificador = (int(a) + int(b) + int(c) + int(d) + int(e)) % 11

print ("%s-%.2d" %(conta, int(verificador)))
