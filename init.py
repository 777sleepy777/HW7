import random
from datetime import datetime, timedelta

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.db import session
from conf.models import Teachers, Students, Subjects, Groups, Grades
fake = Faker('uk-UA')

def insert_teachers():
    for _ in range(10):
        teacher = Teachers(
            full_name = f'{fake.first_name()} {fake.last_name()}'
        )
        session.add(teacher)
        session.commit()

def insert_subjects():
    subjectslist = ['Вища математика', 'Хімія', 'Економіка підприємства', 'Обчислювальна математика',
                   'Історія України',
                   'Теоретична механіка', 'Менеджмент організацій', 'Системне програмування']
    teacherslist = session.query(Teachers).all()
    for i in range(8):
        r = random.randint(1, 10)
        subject = Subjects(
            subjects_name = subjectslist[i],
            teacher_id = teacherslist[r].id
        )
        session.add(subject)
    session.commit()

def insert_groups():
    groups = ['СУА', 'ПЗАС', 'ПН']
    for i in range(3):
        group = Groups(
            group_name=groups[i]
        )
        session.add(group)
    session.commit()

def insert_students():
    grouplist = session.query(Groups).all()
    for i in range(30):
        r = random.randint(0, 2)
        student = Students(
            name = f'{fake.first_name()} {fake.last_name()}',
            group_id = grouplist[r].id
        )
        session.add(student)
    session.commit()

def insert_grads():
    studentlist = session.query(Students).all()
    subjectlist = session.query(Subjects).all()
    start_date = datetime.strptime("2022-09-01", "%Y-%m-%d")
    end_date = datetime.strptime("2023-05-25", "%Y-%m-%d")
    delta = end_date - start_date
    for i in range(100):
        rst = random.randint(0, 59)
        rsu = random.randint(0, 7)
        grad = Grades(
            student_id = studentlist[rst].id,
            subject_id = subjectlist[rsu].id,
            mark = random.randint(0, 11),
            mark_at = start_date + timedelta(random.randint(0, delta.days))
        )
        session.add(grad)
    session.commit()

if __name__ == '__main__':
    try:
        insert_teachers()
        insert_groups()
        insert_subjects()
        insert_students()
        insert_grads()
    except SQLAlchemyError as err:
        print(err)
        session.rollback()
    finally:
        session.close()