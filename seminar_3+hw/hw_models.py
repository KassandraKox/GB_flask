from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Faculty(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    students = db.relationship('Students', backref=db.backref('faculty'), lazy=True)

    def __str__(self):
        return self.title


class Students(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty_pk = db.Column(db.Integer, db.ForeignKey("faculty.pk"), nullable=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Authors(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    books = db.relationship('Book', backref=db.backref('author'), lazy=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Book(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    author_pk = db.Column(db.Integer, db.ForeignKey("authors.pk"), nullable=False)

    def __str__(self):
        return self.title


class NewStudents(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    students = db.relationship('Scores', backref=db.backref('student'), lazy=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Scores(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    student_pk = db.Column(db.Integer, db.ForeignKey("new_students.pk"), nullable=False)
    subject_title = db.Column(db.String(30), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    def __str__(self):
        return self.subject_title


class User(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(30), nullable=False)

    def __str__(self):
        return self.username