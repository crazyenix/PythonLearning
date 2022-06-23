#!/usr/bin/python3
import random
word = input("Введите строку или слово: ")

if "проверка" in word.lower()  : print("В введённой переменной есть слово Прро")
else : print("Мало сисек")

for i in word :
	print(i.swapcase(), end="")
print();

for i in word :
	k = random.randrange(-len(word), len(word))
	print(word[k], " - k(rand) = ", k);
