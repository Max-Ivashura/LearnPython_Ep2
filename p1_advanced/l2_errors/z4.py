def read_file(file_name):
    try:
        with open(file_name, 'r') as f:
            content = f.read()
            print(content)  # Выводим содержимое файла
    except FileNotFoundError as e:
        print("Ошибка: Файл не найден.")
        log_error(f"FileNotFoundError: {e}")
    except IOError as e:
        print("Ошибка: Проблема с чтением файла.")
        log_error(f"IOError: {e}")

def log_error(error_message):
    with open('error_log.txt', 'a') as log_file:
        log_file.write(error_message + '\n')

# Используем функцию для чтения файла
read_file('example.txt')
