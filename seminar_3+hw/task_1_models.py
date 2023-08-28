from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

db = SQLAlchemy()


# id и название факультета.
class Faculty(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), nullable=False)
    student = db.relationship('Students', backref=db.backref('faculty'), lazy=True)

    def __str__(self):
        return self.title


# имя, фамилия, возраст, пол, группа и id факультета
class Students(db.Model):
    pk = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(20), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    gender = db.Column(db.String(1), nullable=False)
    group = db.Column(db.Integer, nullable=False)
    faculty_pk = db.Column(db.Integer, db.ForeignKey('faculty.pk'), nullable=False)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'