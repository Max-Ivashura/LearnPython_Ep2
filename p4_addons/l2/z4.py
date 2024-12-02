import asyncio

async def async_number_generator():
    """Асинхронный генератор, который генерирует числа от 1 до 5."""
    for number in range(1, 6):
        await asyncio.sleep(1)  # Задержка в 1 секунду
        yield number  # Генерация текущего числа

async def main():
    """Главная функция для перебора значений генератора."""
    async for number in async_number_generator():
        print(f"Сгенерировано число: {number}")

if __name__ == "__main__":
    asyncio.run(main())
