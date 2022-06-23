#!/usr/bin/python3


#Угадай лучший автомобиль

print("Угадай лучший автомобиль")
print("Название автомобиля нужно вводить строчными буквами")

response = ""

while response != "toyota" :
	response = input("Какой автомобиль самый лучший?")

print("Ура! Вы угадали!")

k=1
while k<=10:
	k+=1;
	if (k%2) != 0 and k != 3: continue
	#if (k%2) != 0 : break
	print(k)
x = 1
y = 0

if x == True : print("x>0 it's TRUE AND y=0 it's FALSE")
else : print("x>0 it's FALSE AND y=0 it's TRUE")