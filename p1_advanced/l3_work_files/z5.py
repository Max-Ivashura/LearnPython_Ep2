import csv
import os


class Client:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return self.name  # Для вывода достаточно имени

    def __eq__(self, other):
        if isinstance(other, Client):
            return self.name == other.name  # Сравниваем по имени (можно добавить сравнение по телефону)

    def __hash__(self):
        return hash(self.name)  # Используем имя для хеширования


def load_clients_from_csv(file):
    clients = []
    try:
        with open(file, "r") as f:
            csv_reader = csv.reader(f)
            for row in csv_reader:
                if row:  # Проверяем, что строка не пустая
                    clients.append(Client(row[0], row[1]))  # Добавляем клиента с именем и телефоном
            return clients
    except FileNotFoundError:
        print(f'Ошибка: файл "{file}" не найден.')
        return []  # Возвращаем пустой список в случае ошибки


def find_common_clients(file1, file2):
    # Загружаем клиентов из обоих файлов
    clients1 = load_clients_from_csv(file1)
    clients2 = load_clients_from_csv(file2)

    # Находим пересечение
    common_clients = set(clients1).intersection(clients2)
    return common_clients


if __name__ == '__main__':
    file1 = 'files/file1.csv'
    file2 = 'files/file2.csv'

    # Создание файлов с клиентами для тестирования (если файлов нет)
    if not os.path.exists(file1):
        with open(file1, 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['Max', '4950245'])
            csv_writer.writerow(['Dan', '4950240'])
            csv_writer.writerow(['Chan', '4950230'])

    if not os.path.exists(file2):
        with open(file2, 'w', newline='') as f:
            csv_writer = csv.writer(f)
            csv_writer.writerow(['Max', '4950245'])
            csv_writer.writerow(['San', '4950240'])
            csv_writer.writerow(['Chan', '4950230'])

    # Находим общих клиентов
    common_clients = find_common_clients(file1, file2)

    # Выводим результат
    if common_clients:
        print("Клиенты, присутствующие в обоих файлах:")
        for client in common_clients:
            print(client)
    else:
        print("Нет общих клиентов в обоих файлах.")
