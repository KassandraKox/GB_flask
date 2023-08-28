from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


# В таблице "Авторы" должны быть следующие поля: id, имя и фамилия.
class Author(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    books = db.relationship('Books', backref=db.backref('author'), lazy=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


# В таблице "Книги" должны быть следующие поля: id, название, год издания, количество экземпляров и id автора.
class Books(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True)
    year = db.Column(db.Integer)
    count = db.Column(db.Integer)
    author_pk = db.Column(db.Integer, db.ForeignKey("author.pk"))

    def __str__(self):
        return self.title