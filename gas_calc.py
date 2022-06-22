#!/usr/bin/python3
"""
#Длинна маршрута в км
dist = float(input ("Введите длинну маршрута в км: "));
#Литров топрива на 100 км
consum = float(input ("Введите расход топлива л/100км: "));

speed = float(input("Введите среднюю скорость движения в км/ч: "));
disel = float(input("Введите объём бака в литрах: "));
gasTime = float(input ("Введите время необходимое на дозаправку в минутах: ")); #Время на дозаправку
absoluteTime = 0;

result1 = dist / speed * 60;
result2 = disel / consum * 100;
if result2 > dist : absoluteTime = result1 / 60;
else : absoluteTime = ((dist // result2) * gasTime + result1) / 60;

print ("Время затраченное на маршрут: ","%.2f" % absoluteTime);
input("Нажмите \"Enter\" для выхода из программы...")
"""

#Путевой компьютер

programm = "Путевой компьютер, v.0.0.1";

#Переменные

stars = 80			#Количество звёздочек
tabs = 5			#Количество отступов

dist = 0			#Расстояние, которое нужно проехать
speed = 0			#Средняя скорость автомобиля, км/ч
time = 0 			#Время в движении (за рулём)
total_time = 0 		#Общее количество времени в пути

tank = 0 			#Размер бака
consum = 0 			#Средний расход топлива на 100 км
refuels = 0 		#Количество дозаправок
refuel_time = 20 	#Время дозаправки
fuel = 0 			#Сколько затрачено топлива
price = 0 			#Стоимость литра топлива

breaks = 0 			#Количество плановых остановок
break_time = 0 		#Время каждой плановой остановки

#Выводим заголовок
print("\t" * tabs, programm, "\n", "*" * stars);

#Ввод данных пользователем

dist = int(input("Введите расстояние в км: "))
speed = int(input("Планируемая средняя скорость (целое число): "))
consum = float(input("Введите средний расход топлива на 100км: "))
tank = float(input("Объём бака в литрах: "))
price = float(input("Введите стоимость литра топлива: "))
breaks = float(input("Введите количество плановых остановок на маршруте: "))
break_time = float(input("Введите время плановой оставки в минутах среднее: "))

#Производим вычисления

time = dist * 60 / speed 		#Время за рулём
fuel = consum * dist / 100 		#Всего затрачено топлива
refuels = fuel // tank 			#Количество дозаправок
total_time = time + refuels * refuel_time + breaks * break_time #Общее время пути

print("*" * stars, "\n", "\t" * tabs, "Результаты")

print("Время за рулём: ", int(time//60),":", int(time % 60))
print("Общее время в пути: ", int(total_time // 60), ":", int(total_time % 60))
print("Количество дозаправок: ", refuels)
print("Затрачено времени на дозаправку: ", refuels*refuel_time, "минут(ы)")
print("Израсходовано топлива в литрах: ", fuel)
print("Стоимость топлива: ", fuel  * price)
input("Нажмите \"Enter\" для завершения...")