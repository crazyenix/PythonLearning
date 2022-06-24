#!/usr/bin/python3

#Работа с кортежами в python

cars = ("Nissan", "Toyota", "Lexus")
drivers = ("Jane", "Max","Claudia", "John")
drivers += ("Mark","Georg")
sup_cars = ("BMW", "Honda","Mercedes")
cars += sup_cars
tup = (cars,drivers)
print(cars[3][1:4], " - ", drivers)
print(len(tup[1]))

autopark = cars

#Программа из учебника
#Пустой кортеж как условие

cars = ()
if not cars :
	print("У Вас пока нет автомобиля")

#Вывод корежа

cars = ("nissan", "toyota", "lexus")

print("Выводим кортеж функцией print()")

print(cars)

print("Поэлементный перебор кортежа")

for item in cars :
	print(item)

#len() и in

print("Сейча у Вас ", len(cars), " автомобилей")

car = input("Поиск автомобиля: ")

if car in cars :
	print("Автомобиль найден!")
else :
	print("Автомобиля ", car, " у Вас нет")

#Слияние кортежей

new_cars = ("ford", "audi")

all_cars = cars + new_cars

print("Результат слияния: ")
print(all_cars)
print()


print("*" * 15)
a,b,c = cars
*a,b,c = cars
print(a,b,c)
print("*" * 15)

x,*y,z = autopark
#y = autopark[int(len(autopark)/2)]
print(x," - ", y, " - ",z)

print("*" * 15)

x,y = tup
print(x, " - ", y)

t = (1,3,5,6,7,4)
print("sum", sum(t))


#Использование инструмента перебора и def

records = [
("foo", 1, 2),
("bar", "hello"),
("foo", 3, 4),
("oth", "call", 967),
]

def do_foo(x, y) :
	print("foo", x, y)

def do_bar(s) :
	print("bar", s)

def do_other(*variables) :
	print("Other: ", variables)

for tag, *args in records :
	if tag == "foo" : 
		do_foo(*args)
	elif tag == "bar" :
		do_bar(*args)
	else :
		do_other(*args)

line = "nobody:*:-2:-2:Unprivileged User:/var/empty:/usr/bin/false"
uname,*_,fields, homedir, sh = line.split(":")
print("uname: %s\nhome dir: %s\nsh: %s\nfields: %s" % (uname, homedir, sh, fields))