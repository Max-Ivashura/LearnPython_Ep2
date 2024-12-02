import aiofiles
import asyncio

async def read_file(filename):
    """Асинхронная функция, читающая содержимое файла."""
    try:
        async with aiofiles.open(filename, mode='r', encoding='utf-8') as f:
            contents = await f.read()  # Асинхронно читаем содержимое файла
        return contents
    except FileNotFoundError:
        return f"Ошибка: Файл '{filename}' не найден."
    except UnicodeDecodeError:
        return f"Ошибка: Невозможно декодировать файл '{filename}'. Попробуйте другую кодировку."

if __name__ == "__main__":
    filename = "example.txt"  # Замените на путь к вашему файлу
    contents = asyncio.run(read_file(filename))
    print(contents)
