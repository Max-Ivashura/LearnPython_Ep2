from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

# Определяем базу данных
Base = declarative_base()


class Student(Base):
    """Модель студента."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # Связь один-ко-многим
    enrollments = relationship('Enrollment', back_populates='student')

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}')>"


class Enrollment(Base):
    """Модель зачисления на курс."""
    __tablename__ = 'enrollments'

    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey('students.id'), nullable=False)
    course_name = Column(String, nullable=False)

    # Связь с моделью Student
    student = relationship('Student', back_populates='enrollments')

    def __repr__(self):
        return f"<Enrollment(id={self.id}, student_id={self.student_id}, course_name='{self.course_name}')>"


# Создаем базу данных и таблицы
engine = create_engine('sqlite:///school.db')
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()


def add_student(name: str) -> None:
    """Добавляет нового студента в базу данных."""
    new_student = Student(name=name)
    session.add(new_student)
    session.commit()
    print(f"Студент '{name}' добавлен в базу данных.")


def add_enrollment(student_id: int, course_name: str) -> None:
    """Добавляет зачисление студента на курс."""
    new_enrollment = Enrollment(student_id=student_id, course_name=course_name)
    session.add(new_enrollment)
    session.commit()
    print(f"Студент ID {student_id} зачислен на курс '{course_name}'.")


def list_students_and_courses() -> None:
    """Выводит всех студентов и их курсы."""
    students = session.query(Student).all()
    if students:
        print("Студенты и их курсы:")
        for student in students:
            courses = [enrollment.course_name for enrollment in student.enrollments]
            courses_str = ', '.join(courses) if courses else 'Нет курсов'
            print(f"{student.name} (ID: {student.id}): {courses_str}")
    else:
        print("В базе данных нет студентов.")


if __name__ == "__main__":
    # Удаляем все данные при запуске (для тестирования)
    session.query(Enrollment).delete()
    session.query(Student).delete()
    session.commit()

    # Добавление студентов
    add_student("Иван Иванов")
    add_student("Анна Смирнова")

    # Добавление курсов
    add_enrollment(1, "Математика")
    add_enrollment(1, "Физика")
    add_enrollment(2, "Химия")

    # Список студентов и их курсов
    list_students_and_courses()

    # Закрытие сессии
    session.close()
