#!/usr/bin/python3
"""
age = int(input("Enter your age: "))
if age < 18 :
	print("Two lines")
	input("You so young")
elif age == 22 :
	print("22")
else :
	input("Hi Friend.");

mark = 0
while True:
	mark = int(input("Какую оценку ты получил по математике?"))

	if mark == 5 :
		print("Молодец! Так держать!")
	elif mark == 4 :
		print("Хорошо, но могло быть лучше.")
	elif mark == 3 :
		print("Нужно приложить дополнительные усилия.")
	elif mark == 2 :
		print("Обратись за помощью к репетитору.")
	else : break
"""

mark = 0 		#Оценка

if int(input("""Сколько бит в одном байте:
	1) 8
	2) 6
	3) 4
	4) 2
Ваш ответ: """)) == 1 : mark += 1

if int(input("""\nСколько байт в одном килобайте:
	1) 1000
	2) 1024
	3) 1048
	4) 256
Ваш ответ: """)) == 2 : mark += 1

if int(input("""\nКомпания-разработчик Windows:
	1) Mikrosoft
	2) Melkosoft
	3) Cybersoft
	4) Microsoft
Ваш ответ: """)) == 4 : mark += 1

if int(input("""\nСамая "яблочная" ОС:
	1) AppleOS
	2) Linux
	3) macOS
	4) FreeBSD
Ваш ответ: """)) == 3 : mark += 1
if int(input("""\nСимволом какой ОС является пингвин:
	1) Linux
	2) FreeBSD
	3) OS/2
	4) Windows
Ваш ответ: """)) == 1 : mark += 1

print("\nВаша оценка: ", mark)