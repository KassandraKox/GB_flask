from hw_tasks import app
import hw_models
import hw_text_storage as storage


@app.cli.command('init-db')
def init_db():
    hw_models.db.create_all()
    hw_models.db.session.close()
    print('DB is created')


@app.cli.command('fill-students')
def fill_students():
    for faculty in storage.faculties:
        new_faculty = hw_models.Faculty(title=faculty)
        hw_models.db.session.add(new_faculty)
    hw_models.db.session.commit()

    for student in storage.students:
        first_name, last_name, age, gender, group, faculty = student
        new_student = hw_models.Students(first_name=first_name,
                                         last_name=last_name,
                                         age=age,
                                         gender=gender,
                                         group=group,
                                         faculty_pk=faculty)
        hw_models.db.session.add(new_student)
    hw_models.db.session.commit()
    print('Students DB is filled')


@app.cli.command('fill-books')
def fill_books():
    for author in storage.authors:
        new_author = hw_models.Authors(first_name=author[0],
                                       last_name=author[1])
        hw_models.db.session.add(new_author)
    hw_models.db.session.commit()

    for book in storage.books:
        new_book = hw_models.Book(title=book[0],
                                  year=book[1],
                                  count=book[2],
                                  author_pk=book[3])
        hw_models.db.session.add(new_book)
    hw_models.db.session.commit()
    print('Books DB is filled')


@app.cli.command('fill-new-students')
def fill_new_students():
    for student in storage.new_students:
        new_student = hw_models.NewStudents(first_name=student[0],
                                            last_name=student[1],
                                            group=student[2],
                                            email=student[3])
        hw_models.db.session.add(new_student)
    hw_models.db.session.commit()

    for score in storage.scores:
        new_score = hw_models.Scores(student_pk=score[0],
                                     subject_title=score[1],
                                     score=score[2])
        hw_models.db.session.add(new_score)
    hw_models.db.session.commit()
    print('Students DB is filled')


if __name__ == '__main__':
    init_db()
    # fill_students()
    # fill_books()
    # fill_new_students()