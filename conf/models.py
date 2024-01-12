from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, event
from sqlalchemy.orm import relationship, declarative_base

from database.db import engine

Base = declarative_base()

class Groups(Base):
    __tablename__ = 'groups'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(25), nullable=False, unique=True)

class Students(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    name = Column(String(25), nullable=False, unique=True)
    group_id = Column(Integer, ForeignKey('groups.id'))
    group = relationship(Groups)

class Teachers(Base):
    __tablename__ = 'teachers'
    id = Column(Integer, primary_key=True)
    full_name = Column(String(25), nullable=False, unique=True)

class Subjects(Base):
    __tablename__ = 'subjects'
    id = Column(Integer, primary_key=True)
    subjects_name = Column(String(25), nullable=False, unique=True)
    teacher_id = Column(Integer, ForeignKey('teachers.id'), onupdate='CASCADE')
    teacher = relationship(Teachers, backref='subjects')

class Grades(Base):
    __tablename__ = 'grades'
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'))
    student = relationship(Students, backref='mark')
    subject_id = Column(Integer, ForeignKey('subjects.id'))
    subject = relationship(Subjects, backref='mark')
    mark = Column(Integer)
    mark_at = Column(DateTime, default=func.now())

@event.listens_for(Grades, 'before_update')
def update_updated_at(mapper, conn, target):
    target.mark_at = func.now()

Base.metadata.create_all(engine)
