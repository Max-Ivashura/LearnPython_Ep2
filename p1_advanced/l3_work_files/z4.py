def open_file(filename):
    try:
        # Пытаемся открыть файл для чтения
        with open(filename, "r") as f:
            print(f.read())
    except FileNotFoundError:
        # Обработка исключения: файл не найден
        print(f'Ошибка: Файл "{filename}" не найден.')
        # Создание файла и запись сообщения об ошибке
        with open(filename, 'w') as f:
            f.write(f'Ошибка: Файл не найден.\n')
            f.write(f'Попытка открыть файл: {filename}\n')


if __name__ == "__main__":
    open_file('files/non_existent_file.txt')
