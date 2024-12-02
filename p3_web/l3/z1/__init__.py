import sqlite3


def create_db() -> None:
    """Создаёт таблицу студенты."""
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        age INTEGER NOT NULL,
        grade INTEGER NOT NULL
    )
    ''')
    conn.commit()


def insert_db(students: list) -> None:
    cursor.executemany('''
    INSERT INTO students (name, age, grade) VALUES (?, ?, ?)
    ''', students)

    # Подтвердите изменения
    conn.commit()


def select(mark: int) -> list:
    """Запрашивает студентов с оценкой выше заданной.
        :param mark: Оценка для запроса
    """
    cursor.execute(f'SELECT * FROM students WHERE grade > {mark}')
    high_grade_students = cursor.fetchall()
    return high_grade_students


def update(age: int, id: int) -> None:
    """Обновляет возраст студента по его идентификатору.
        :param age: Возраст ученика
        :param id: Идентификатор ученика
    """
    cursor.execute('UPDATE students SET age = ? WHERE id = ?', (age, id))
    conn.commit()


def delete(id: int) -> None:
    """Удаляет студента по его идентификатору.
            :param id: Идентификатор ученика
    """
    cursor.execute('DELETE FROM students WHERE id = ?', (id,))
    conn.commit()


if __name__ == '__main__':
    # Вставьте данные о студентах
    students_to_insert = [
        ('Alice', 20, 85),
        ('Bob', 19, 70),
        ('Charlie', 22, 90),
        ('David', 21, 65),
        ('Eve', 20, 75)
    ]

    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()
    mark = 70

    students = select(mark)
    print('Студенты, у которых оценка выше заданной:')
    for student in students:
        print(student)

    update(30, 2)

    conn.close()
