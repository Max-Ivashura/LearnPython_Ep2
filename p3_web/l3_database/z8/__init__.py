import csv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Настройка базы данных и ORM
Base = declarative_base()
engine = create_engine('sqlite:///students.db')
Session = sessionmaker(bind=engine)
session = Session()

class Student(Base):
    """Модель студента."""
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    grade = Column(String, nullable=False)

    def __repr__(self):
        return f"<Student(id={self.id}, name='{self.name}', age={self.age}, grade='{self.grade}')>"

# Создание таблицы
Base.metadata.create_all(engine)

def load_students_from_csv(file_path: str) -> None:
    """Загружает студентов из CSV файла и добавляет их в базу данных."""
    with open(file_path, mode='r', encoding='cp1251') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            new_student = Student(name=row['name'], age=int(row['age']), grade=row['grade'])
            session.add(new_student)
            print(f"Добавлен студент: {new_student}")
    session.commit()

# Основной блок программы
if __name__ == "__main__":
    # Загружаем студентов из CSV файла
    load_students_from_csv('students.csv')

    # Выводим всех студентов
    students = session.query(Student).all()
    print("\nСписок студентов в базе данных:")
    for student in students:
        print(student)

    # Закрытие сессии
    session.close()
