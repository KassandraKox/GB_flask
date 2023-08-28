# Создать базу данных для хранения информации о книгах в библиотеке.
# База данных должна содержать две таблицы: "Книги" и "Авторы".
# В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
# Необходимо создать связь между таблицами "Книги" и "Авторы". Написать функцию-обработчик,
# которая будет выводить список всех книг с указанием их авторов.

from flask import Flask, render_template

from task_2_models import db, Author, Books

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db2.db'
db.init_app(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books/')
def all_books():
    authors = Author.query.all()
    books = Books.query.all()

    context = {
        'title': 'Список студентов',
        'books': books,
    }

    return render_template('all_books.html', **context)


@app.cli.command('init-db')
def init_db():
    db.create_all()
    print('OK')


BOOKS = [
    ['Book 1', 2000, 2, 1],
    ['Book 2', 2001, 21, 2],
    ['Book 3', 2002, 6, 1],
    ['Book 4', 2003, 1, 2],
    ['Book 5', 2004, 5, 1],
]

AUTHORS = [
    ['John', 'Smith'],
    ['Jane', 'Krow'],
]


@app.cli.command('fill-db')
def fill_tables():
    for author in AUTHORS:
        new_author = Author(first_name=author[0], last_name=author[1])
        db.session.add(new_author)
    db.session.commit()

    for book in BOOKS:
        new_book = Books(title=book[0], year=book[1], count=book[2], author_pk=book[3])
        db.session.add(new_book)
    db.session.commit()


if __name__ == '__main__':
    app.run(debug=True)