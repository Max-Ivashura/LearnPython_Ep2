from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import datetime

# Определяем базу данных и создаем её
Base = declarative_base()

class Author(Base):
    """Модель автора."""
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birth_date = Column(Date)

    def __repr__(self):
        return f"<Author(name='{self.name}', birth_date='{self.birth_date}')>"

# Создаём базу данных и таблицы
engine = create_engine('sqlite:///library.db')
Base.metadata.create_all(engine)

# Создание сессии для работы с базой данных
Session = sessionmaker(bind=engine)
session = Session()

# Добавление авторов
authors_to_add = [
    Author(name='George Orwell', birth_date=datetime.date(1903, 6, 25)),
    Author(name='Harper Lee', birth_date=datetime.date(1926, 4, 28)),
    Author(name='F. Scott Fitzgerald', birth_date=datetime.date(1896, 9, 24)),
    Author(name='Herman Melville', birth_date=datetime.date(1819, 8, 1)),
    Author(name='Jane Austen', birth_date=datetime.date(1775, 12, 16)),
]

session.add_all(authors_to_add)
session.commit()

# Вывод всех авторов из базы данных
authors = session.query(Author).all()
print("Авторы в базе данных:")
for author in authors:
    print(author)

# Закрытие сессии
session.close()
