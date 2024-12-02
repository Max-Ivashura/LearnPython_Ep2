import csv


class Student:
    def __init__(self, name: str, age: int, special: str):
        self.name = name
        self.age = age
        self.special = special

    def to_row(self):
        return [self.name, self.age, self.special]


def write_students_to_csv(filename: str, students: list):
    """Записывает студентов в CSV-файл."""
    with open(filename, 'w', newline='') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(['Name', 'Age', 'Specialty'])  # Запись заголовков
        for student in students:
            csv_writer.writerow(student.to_row())


def read_students_from_csv(filename: str):
    """Читает студентов из CSV-файла и выводит информацию на экран."""
    with open(filename, 'r') as f:
        csv_reader = csv.reader(f)
        next(csv_reader)  # Пропустить заголовки
        for row in csv_reader:
            print(f'Name: {row[0]}, Age: {row[1]}, Specialty: {row[2]}')


if __name__ == '__main__':
    filename = 'files/students.csv'
    # Создание списка студентов
    students = [
        Student('Max', 18, 'Programmer'),
        Student('Vika', 14, 'Policeman'),
        Student('Skif', 19, 'Manager')
    ]
    write_students_to_csv(filename, students)  # Запись студентов в файл
    read_students_from_csv(filename)  # Чтение студентов из файла
