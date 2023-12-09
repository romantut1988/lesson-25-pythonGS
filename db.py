import sqlite3

conn = sqlite3.connect('database.db')  # предоставляю файл с БД

print("open database")  # сообщение о выводе запуска

conn.execute("CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)")

print("create table")  # сообщение о создании таблицы

conn.close()  # закрываем соединение с БД
