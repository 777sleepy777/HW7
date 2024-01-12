from conf.models import Grades, Teachers, Students, Groups, Subjects
from conf.db import session
from sqlalchemy import func, desc

def select_01():
       result = session.query(Students.name, func.round(func.avg(Grades.mark), 2).label('avg_grade')) \
                .select_from(Groups).join(Students).group_by(Students.id).order_by(desc('avg_grade')).limit(5).all()
       return result

def select_02():
       result = session.query(Students.name, func.round(func.avg(Grades.mark), 2).label('avg_grade')) \
                .select_from(Grades).join(Students).filter(Grades.subject_id==19).group_by(Students.id).order_by(desc('avg_grade')).limit(1).all()
       return result

def select_03():
       result = session.query(Groups.group_name, func.round(func.avg(Grades.mark), 2).label('avg_grade')) \
                .select_from(Grades).join(Students).join(Groups).filter(Grades.subject_id==19).group_by(Groups.id).order_by(desc('avg_grade')).limit(1).all()
       return result


def select_04():
    result = session.query(func.round(func.avg(Grades.mark), 2).label('avg_grade')) \
        .select_from(Grades).all()
    return result


def select_05():
    result = session.query(Subjects.id, Subjects.subjects_name) \
        .select_from(Subjects).join(Teachers).filter(Teachers.id==26).group_by(Subjects.id).order_by(
        Subjects.id).all()
    return result

def select_06():
    result = session.query(Students.id, Students.name, Groups.id) \
            .select_from(Students).join(Groups).filter(Groups.id==2).order_by(
        Students.id).all()
    return result

def select_07():
    result = session.query(Groups.id, Students.id, Students.name, Subjects.subjects_name, Grades.mark) \
            .select_from(Grades).join(Students).join(Groups).join(Subjects).filter(Groups.id==2, Subjects.id == 19).all()
    return result


def select_08():
    result = session.query(Subjects.subjects_name, func.round(func.avg(Grades.mark), 2).label('avg_grade')) \
        .select_from(Grades).join(Subjects).join(Teachers).filter(Teachers.id==26).group_by(Subjects.subjects_name).order_by(desc('avg_grade')).all()
    return result

def select_09():
    result = session.query(Subjects.subjects_name) \
        .select_from(Grades).join(Subjects).join(Students).filter(Students.id==38).group_by(Subjects.subjects_name).all()
    return result

def select_10():
    result = session.query(Subjects.subjects_name) \
        .select_from(Grades).join(Subjects).join(Students).join(Teachers).filter(Students.id==38, Teachers.id==5).group_by(Subjects.subjects_name).all()
    return result



