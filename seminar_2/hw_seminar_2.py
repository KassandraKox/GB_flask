from flask import Flask, render_template, request, redirect, url_for, flash, session

import hw_seminar_2_text_storage as storage

app = Flask(__name__)
app.secret_key = b'97b3c2a38768bfbd184ca8e63d5fe2bb144470985bad9911e79e832ce36d280d'


@app.route("/")
def index():
    context = storage.index_tasks

    return render_template("index.html", **context)


@app.route("/age_check/", methods=["GET", "POST"])
def age_check():
    context = {"title": "Задача номер 6", }

    if request.method == "POST":
        name = request.form.get("name")
        age = int(request.form.get("age"))
        if 18 <= age <= 100:
            return redirect(url_for("age_check_success", name=name))
        else:
            return redirect(url_for("age_check_fail"))

    return render_template("age_check.html", **context)


@app.route("/age_check/success/")
def age_check_success():
    context = {
        "title": "Успешная проверка возраста",
        "name": request.args.get("name"),
    }

    return render_template("age_check_success.html", **context)


@app.route("/age_check/fail/")
def age_check_fail():
    context = {"title": "Неудачная проверка возраста", }

    return render_template("age_check_fail.html", **context)


@app.route("/num_to_sqrt/", methods=["GET", "POST"])
def num_to_sqrt():
    context = {"title": "Задача номер 7", }

    if request.method == "POST":
        num = int(request.form.get("num"))
        return redirect(url_for("num_to_sqrt_result", num=num, sqrt=int(num) ** 2))

    return render_template("num_to_sqrt.html", **context)


@app.route("/num_to_sqrt/result/")
def num_to_sqrt_result():
    context = {
        "title": "Результат задачи номер 7",
        "num": request.args.get("num"),
        "sqrt": request.args.get("sqrt"),
    }

    return render_template("login.html", **context)


@app.route("/flash_task/", methods=["GET", "POST"])
def flash_task():
    context = {"title": "Задача номер 8", }

    if request.method == "POST":
        flash('Форма успешно отправлена!', 'success')
        return redirect(url_for("flash_task"))

    return render_template("flash_task.html", **context)


@app.route("/cookie_task/", methods=["GET", "POST"])
def cookie_task():
    context = {"title": "Задача номер 9", }

    if request.method == "POST":
        session['user_name'] = request.form.get("name")
        session['user_email'] = request.form.get("email")
        name = session['user_name']
        return redirect(url_for("hello_page"))

    return render_template("cookie_task.html", **context)


@app.route("/cookie_task/hello_page/")
def hello_page():
    context = {
        "title": "Успешных вход",
        "name": session['user_name'],
    }

    return render_template("hello_page.html", **context)


@app.route("/cookie_task/logout/")
def logout():
    context = {
        "title": "Успешный выход",
        "name": session['user_name']
    }
    session.pop('user_name', None)
    session.pop('user_email', None)

    return render_template('logout.html', **context)


app.run(debug=True)