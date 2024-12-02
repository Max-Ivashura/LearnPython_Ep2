from sqlalchemy import create_engine, Column, Integer, String, exc
from sqlalchemy.orm import declarative_base, sessionmaker

# Настройка базы данных и ORM
Base = declarative_base()
engine = create_engine('sqlite:///customers.db')
Session = sessionmaker(bind=engine)
session = Session()


class Customer(Base):
    """Модель клиента."""
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)  # Уникальное поле

    def __repr__(self):
        return f"<Customer(id={self.id}, name='{self.name}', email='{self.email}')>"


# Создание таблицы
Base.metadata.create_all(engine)


def add_customer(name: str, email: str) -> None:
    """Добавляет нового клиента в базу данных."""
    new_customer = Customer(name=name, email=email)
    session.add(new_customer)
    try:
        session.commit()
        print(f"Клиент '{name}' с email '{email}' добавлен в базу данных.")
    except exc.IntegrityError:
        session.rollback()  # Откат транзакции
        print(f"Ошибка: Клиент с email '{email}' уже существует.")


def list_customers() -> None:
    """Выводит всех клиентов."""
    customers = session.query(Customer).all()
    if customers:
        print("Список клиентов:")
        for customer in customers:
            print(f"{customer.name} (ID: {customer.id}, Email: {customer.email})")
    else:
        print("В базе данных нет клиентов.")


# Основной блок программы
if __name__ == "__main__":
    # Пример добавления клиентов
    add_customer("Иван Иванов", "ivan@example.com")
    add_customer("Анна Смирнова", "anna@example.com")

    # Попытка добавить клиента с существующим email
    add_customer("Петр Петров", "ivan@example.com")  # Дублирование email

    # Вывод списка клиентов
    list_customers()

    # Закрытие сессии
    session.close()
