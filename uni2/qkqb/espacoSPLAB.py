#coding: utf-8

user1 = raw_input()
espUser1 = float(input())
user2 = raw_input()
espUser2 = float(input())
user3 = raw_input()
espUser3 = float(input())

user1MB = (espUser1 / 1024) / 1024
user2MB = (espUser2 / 1024) / 1024
user3MB = (espUser3 / 1024) / 1024
total = user1MB + user2MB + user3MB
media = total / 3

print ("SPLab - Espaço utilizado pelos usuários")
print ("---------------------------------------------")
print ("Nr., Usuário, Espaço Utilizado")
print ("")

print ("1, %s, %.2f MB" %(user1, user1MB))
print ("2, %s, %.2f MB" %(user2, user2MB))
print ("3, %s, %.2f MB" %(user3, user3MB))
print ("")

print ("Espaço total ocupado: %.2f MB" %total)
print ("Espaço médio ocupado: %.2f MB" %media)
