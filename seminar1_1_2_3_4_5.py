# Задача 1
# Напишите простое веб-приложение на Flask, которое будет выводить на экран текст "Hello, World!".
#
# Задача 2
# Добавьте две дополнительные страницы в ваше вебприложение:
# страницу "about"
# страницу "contact".
#
# Задача 3
# Написать функцию, которая будет принимать на вход два числа и выводить на экран их сумму.
#
# Задача 4
# Написать функцию, которая будет принимать на вход строку и выводить на экран ее длину.
#
# Задача 5
# Написать функцию, которая будет выводить на экран HTML страницу с заголовком "Моя первая HTML страница" и
# абзацем "Привет, мир!".

from main_sem1 import app


@app.route('/')
def index():
    return "Hello World"


@app.route('/about/')
def about():
    return "About page"


@app.route('/contact/')
def contact():
    return "Contact page"


@app.route("/sum/<int:num1>-<int:num2>/")
def sum_num(num1, num2):
    res = num1 + num2
    return f"{num1} + {num2} = {res}"


@app.route("/len/<text>/")
def len_text(text):
    return f"{len(text)}"


@app.route("/first-page/")
def first_page():
    return ("<h1>Моя первая HTML страница</h1>"
            "<p>Привет, мир!</p>")


app.run(debug=True)