# Задание 6
# Написать функцию, которая будет выводить на экран HTML страницу с таблицей, содержащей информацию о студентах.
# Таблица должна содержать следующие поля: "Имя", "Фамилия", "Возраст", "Средний балл".
# Данные о студентах должны быть переданы в шаблон через контекст
from flask import render_template

from main_sem1 import app


@app.route('/students/')
def students():
    context = {
        "students": [{"first_name": "Иван",
                      "last_name": "Иванов",
                      "age": 30,
                      "grade": 5, },
                     {
                         "first_name": "Максим",
                         "last_name": "Максимов",
                         "age": 35,
                         "grade": 2,
                     },
                     {
                         "first_name": "Андрей",
                         "last_name": "Андреев",
                         "age": 25,
                         "grade": 7,
                     }]
    }
    return render_template("students.html", **context)


app.run(debug=True)