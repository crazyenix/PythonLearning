#!/usr/bin/python3

level = 0 		#Уровень доступа

login = ""
password = ""

while not login:
	login = input("Введите логин пользователя: ")

while not password:
	password = input("Введите пароль пользователя: ")

if login == "root" and password == "toor" : level = 10
elif login == "user" and password == "resu" : level = 5

if level :
	print("Привет, ", login)
	print("Твой уровень доступа: ", level)
else :
	print("Доступ закрыт!")