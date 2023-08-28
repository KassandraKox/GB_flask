# Создать базу данных для хранения информации о студентах университета.
# База данных должна содержать две таблицы: "Студенты" и "Факультеты".
# В таблице "Студенты" должны быть следующие поля: id, имя, фамилия, возраст, пол, группа и id факультета.
# В таблице "Факультеты" должны быть следующие поля: id и название факультета.
# Необходимо создать связь между таблицами "Студенты" и "Факультеты".
# Написать функцию-обработчик, которая будет выводить список всех студентов с указанием их факультета.

from flask import Flask, render_template

from task_1_models import db, Students, Faculty

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/students/')
def all_students():
    students = Students.query.all()
    faculties = Faculty.query.all()

    context = {
        'students': students,
        'title': 'Список студентов',
        'faculties': faculties,
    }

    return render_template('all_students.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


STUDENTS = [
    ['Ivan', 'Ivanov', 30, 'M', 101, 1],
    ['Maria', 'Andreeva', 25, 'F', 102, 1],
    ['Maksim', 'Maksimov', 22, 'M', 201, 2],
    ['Evgenii', 'Evgenev', 31, 'M', 203, 2],
    ['Olga', 'Olegovna', 34, 'F', 101, 1],
]
FACULTIES = ['Engineers', 'Economists']


@app.cli.command('fill-db')
def fill_tables():
    for faculty in FACULTIES:
        new_faculty = Faculty(title=faculty)
        db.session.add(new_faculty)
    db.session.commit()

    for student in STUDENTS:
        first_name, last_name, age, gender, group, faculty = student
        new_student = Students(first_name=first_name, last_name=last_name, age=age, gender=gender, group=group,
                               faculty_pk=faculty)
        db.session.add(new_student)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)