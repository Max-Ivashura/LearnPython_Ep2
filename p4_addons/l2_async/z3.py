import asyncio


async def fetch_data(url):
    """Асинхронная функция, имитирующая медленную загрузку данных с указанного URL."""
    print(f"Начало загрузки данных с {url}...")
    # Имитация медленной операции сети
    await asyncio.sleep(2)  # Замена на 2 секунды ожидания
    print(f"Загрузка завершена для {url}.")
    return f"Данные с {url}"


async def main():
    """Главная функция для запуска параллельных задач."""
    # Список URL для загрузки
    urls = [
        "http://example.com/data1",
        "http://example.com/data2",
        "http://example.com/data3"
    ]

    # Создаем список задач
    tasks = [fetch_data(url) for url in urls]

    # Запускаем все задачи параллельно и ждем их завершения
    results = await asyncio.gather(*tasks)

    # Выводим результаты
    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())
