import asyncio


async def print_numbers():
    """Асинхронная функция, выводящая числа от 1 до 5 с задержкой в 1 секунду."""
    for i in range(1, 6):
        print(i)
        await asyncio.sleep(1)  # Задержка в 1 секунду


if __name__ == "__main__":
    asyncio.run(print_numbers())
