#!/usr/bin/python3
import re
import random
import os
from fnmatch import fnmatch, fnmatchcase


#re.split - проба работы с разделителем строк на составляющие
#значение line выводится в консоль или же присваивается переменной
#которая в свою очередь станет списком
print("\v", "*" * 20, "\tre.split(r'[;,\\s]\\s*', line\t", "*" * 20, "\v")

line = "asdf fjdk;afed,fjtk,asdf, foo"

print(re.split(r'[;,\s]\s*', line))

#Использование маски оболочки. Поиск совпадения в списке
#используя модуль fnmatch - fnmatch, fnmatchcase
#

print("\v", "*" * 20, "\tfnmatch(name, 'Dat*.csv')\t", "*" * 20, "\v")

names = ["Dat1.csv", "Dat2.csv", "config.ini", "rep.py"]

#[name for name in names if fnmatch(name, "Dat*.csv")] - работает только в консоли

for name in names :
	if fnmatch(name, "Dat*.csv") :
		print(name)

#Проверка и поиск совпадений в начале строки str.startswith()
#поиск онного в конце str.endswith()
#for i in list : if i.strswith

print("\v", "*" * 20, "\tfnmatch(name, 'Dat*.csv')\t", "*" * 20, "\v")

filename = "capricot.rep"
print(filename.startswith("ca")) #true
print(filename.endswith("res")) #false

#Программка просмотра содержимого каталогов
dir_check = "" #контрольная переменна для промежуточного сохранения пути
filenames = "" #переменная получения списка имён содержимого каталога

#Функция перебора списка полученного содержимого каталока
def folder(d) :
	for item in filenames :
				if item.endswith("py") :
					print ("\t- ",item)
				else : 
					print(" - [F] - ", item)

while True :	#Тело цикла
	i = 0
	dir_user = input("Введите название каталога или exit для выхода: ")
	if dir_user == "exit" : break #Выход из программы
	if filenames != ""  : #Проверка на первый запуск программы
		for item in filenames : #проход списка полученных имён на совпадения
			if item == dir_user :  #Совпало - в путь!
				dir_check += "/" + dir_user #Сохраняем промежуточные данные пути обновляя их
				filenames = os.listdir(dir_check) #Получаем имена содержимого
				folder(filenames) #Функция вывода данных в консоль
				i = 1 #Контрольная переменная, для игнорирования последующего вывода данных после сброса цикал
				break
	try :
		if i == 0 :
			filenames = os.listdir(dir_user)
			dir_check = dir_user
			folder(filenames)
	except (OSError, IOError):
		print("Не верный путь!")