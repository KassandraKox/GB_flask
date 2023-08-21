# Задача 1
# Создать страницу, на которой будет кнопка "Нажми меня",
# при нажатии на которую будет переход на другую страницу с приветствием пользователя по имени.,

# Задача 2
# Создать страницу, на которой будет изображение и ссылка на другую страницу,
# на которой будет отображаться форма для загрузки изображений.

# Задача 3
# Создать страницу, на которой будет форма для ввода логина и пароля
# При нажатии на кнопку "Отправить" будет произведена проверка соответствия логина и пароля и
# переход на страницу приветствия пользователя или страницу с ошибкой.

# Задача 4
# Создать страницу, на которой будет форма для ввода текста и кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов в тексте и переход на страницу с результатом.

# Задача 5
# Создать страницу, на которой будет форма для ввода двух чисел и выбор операции
# (сложение, вычитание, умножение или деление) и кнопка "Вычислить"
# При нажатии на кнопку будет произведено вычисление результата выбранной операции и переход на страницу с результатом.
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index_seminar.html')


@app.route('/hello/')
def hello_page(name=None):
    context = {
        'name': name or 'John'
    }

    return render_template('hello.html', **context)


@app.route('/form/', methods=['GET', 'POST'])
def form_page():
    if request.method == 'POST':
        name = request.form.get('name')
        password = request.form.get('password')
        if name == "John" and password == "pass":
            return redirect(url_for('hello_page', name=name))
        return render_template('form_page.html', error=True)
    return render_template('form_page.html', error=None)


@app.route('/text-form/', methods=['GET', 'POST'])
def text_form_page():
    if request.method == 'POST':
        text = request.form.get('text')
        return redirect(url_for('text_page', text_1=text))
    return render_template('text_form_page.html')


@app.route('/text-page/')
def text_page():
    text_1 = request.args.get("text_1")
    word_count = text_1.split()
    context = {
        'text': text_1,
        'len_text': len(word_count)
    }
    return render_template('text_page.html', **context)


@app.route('/calc/', methods=['GET', 'POST'])
def calc():
    if request.method == 'POST':
        num1 = int(request.form.get('num1'))
        num2 = int(request.form.get('num2'))
        opt = request.form.get('opt')
        match opt:
            case 'plus':
                res = num1 + num2
            case 'minus':
                res = num1 - num2
            case 'prod':
                res = num1 * num2
            case 'div':
                res = num1 / num2
        return render_template('calc_form_page.html', res=res)
    return render_template('calc_form_page.html', res=None)


app.run(debug=True)