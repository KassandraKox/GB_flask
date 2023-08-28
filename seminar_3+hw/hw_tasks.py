from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf import CSRFProtect
from sqlalchemy import or_

import hw_text_storage as storage
import hw_models
import hw_forms

app = Flask(__name__)
app.secret_key = b'97b3c2a38768bfbd184ca8e63d5fe2bb144470985bad9911e79e832ce36d280d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hw_db.db'
hw_models.db.init_app(app)
csrf = CSRFProtect(app)


@app.route("/")
def index():
    context = storage.index_tasks

    return render_template("index.html", **context)


@app.route('/all-students/')
def all_students():
    faculties = hw_models.Faculty.query.all()
    students = hw_models.Students.query.all()

    context = {
        'faculties': faculties,
        'students': students,
        'title': "Все студенты",
    }

    return render_template('all_students.html', **context)


@app.route('/all-books/')
def all_books():
    book_list = [hw_models.Book.query.filter(hw_models.Book.author_pk == author.pk).all()
                 for author in hw_models.Authors.query.all()]

    context = {
        'book_list': book_list,
        'title': "Все книги",
    }

    return render_template('all_books.html', **context)


@app.route('/new-students/')
def new_students():
    scores_list = {}
    for student in hw_models.NewStudents.query.all():
        temp = hw_models.Scores.query.filter(hw_models.Scores.student_pk == student.pk).all()
        scores_list[student] = temp or []

    context = {
        'scores_list': scores_list,
        'title': "Студенты и оценки",
    }

    return render_template('new_students.html', **context)


@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = hw_forms.RegisterForm()
    if request.method == 'POST' and form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        existing_user = hw_models.User.query.filter(
            or_(hw_models.User.username == username, hw_models.User.email == email)).first()

        if existing_user:
            flash('User with this username or email is already registered', 'danger')
            return redirect(url_for("register", form=form))
        else:
            new_user = hw_models.User(username=username, email=email, password=password)
            hw_models.db.session.add(new_user)
            hw_models.db.session.commit()
            return redirect(url_for("register_success", username=username))

    context = {
        'form': form,
        'title': 'Register Page'
    }

    return render_template('register.html', **context)


@app.route('/register-success/')
def register_success():
    username = request.args.get('username')

    context = {
        'username': username,
        'title': 'Register success'
    }

    return render_template('register-success.html', **context)


if __name__ == '__main__':
    app.run(debug=True)