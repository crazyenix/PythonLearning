#!/usr/bin/python3
#import random
import random

print("*" * 10, "Угадай число", "*" * 10)
print("Компьютер будет загадывать число от 1 до 10. Попробуй угадать число. Для выхода введи 0")

answer = 1
score = 0
i = 0 
k = 0
while answer:
	i += 1
	k = 0
	answer = 1
	rand = random.randint(1, 10)
	while answer != rand and answer:
		k += 1
		answer = int(input("Введите ваше число: "))
		if answer == rand :
			score += 1
		elif answer != rand and answer :
			print("Не правиль. Ещё раз!?")
	if answer == rand : print("Правильно! Всего за ", k," попыток!\nКомпьютер загадал новое число!")
	
print("Спасибо за игру!\n Угадали ", score," чисел из ", i,"\nЕщё увидимся!")