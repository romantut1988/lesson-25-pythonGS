from flask import Flask, render_template, request

import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('student.html')


@app.route('/addrec', methods=["POST", "GET"])
def addrec():
    if request.method == "POST":  # проверка метода запроса
        try:
            nm = request.form['nm']  # метод запроса для получения имя
            addr = request.form['add']  # метод запроса для получения адрес
            city = request.form['city']  # метод запроса для получения города
            pin = request.form['pin']  # метод запроса для получения пинкода

            with sql.connect("database.db") as con:  # подключение или коннект к БД

                cur = con.cursor()  # новый метод вставки

                cur.execute("INSERT INTO students (name, addr, city, pin) VALUES (?, ?, ?, ?)", (nm, addr, city, pin))

                con.commit()  # точка фиксации изменения

                msg = "Сообщение успешно добавлено"  # сообщение об добавлении

        except:
            con.rollback()  # сообщение об откате если будет ошибка
            msg = "Ошибка операции"

        finally:  # обязательное поле об завершении
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row  # метод добавления запросов

    cur = con.cursor()

    cur.execute("select * from students")

    rows = cur.fetchall()  # выводим все параметры введеных запросов

    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)  # перезагружаем приложение при добавлении данных
