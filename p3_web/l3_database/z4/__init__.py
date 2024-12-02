from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Определяем базу данных
Base = declarative_base()


class Movie(Base):
    """Модель фильма."""
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    director = Column(String, nullable=False)
    release_year = Column(Integer, nullable=False)

    def __repr__(self):
        return f"<Movie(id={self.id}, title='{self.title}', director='{self.director}', release_year={self.release_year})>"


# Создаем базу данных и таблицы
engine = create_engine('sqlite:///movies.db')
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()


def add_movie(title: str, director: str, release_year: int) -> None:
    """Добавляет новый фильм в базу данных."""
    new_movie = Movie(title=title, director=director, release_year=release_year)
    session.add(new_movie)
    session.commit()
    print(f"Фильм '{title}' добавлен в базу данных.")


def update_movie(movie_id: int, title: str, director: str, release_year: int) -> None:
    """Обновляет данные о фильме."""
    movie = session.get(Movie, movie_id)
    if movie:
        movie.title = title
        movie.director = director
        movie.release_year = release_year
        session.commit()
        print(f"Фильм ID {movie_id} обновлён.")
    else:
        print(f"Фильм ID {movie_id} не найден.")


def delete_movie(movie_id: int) -> None:
    """Удаляет фильм из базы данных."""
    movie = session.get(Movie, movie_id)
    if movie:
        session.delete(movie)
        session.commit()
        print(f"Фильм ID {movie_id} удалён из базы данных.")
    else:
        print(f"Фильм ID {movie_id} не найден.")


def drop_all_data() -> None:
    """Удаляет все данные из таблицы movies."""
    session.query(Movie).delete()
    session.commit()
    print("Все данные из таблицы movies были удалены.")


def list_movies() -> None:
    """Выводит все фильмы в базе данных."""
    movies = session.query(Movie).all()
    if movies:
        print("Фильмы в базе данных:")
        for movie in movies:
            print(movie)
    else:
        print("В базе данных нет фильмов.")


if __name__ == "__main__":
    # Удаляем все данные при каждом запуске
    drop_all_data()

    # тестирование функций
    list_movies()  # Выводим фильмы (должно быть пусто)

    # Добавление фильмов
    add_movie("Inception", "Christopher Nolan", 2010)
    add_movie("The Matrix", "Lana Wachowski, Lilly Wachowski", 1999)
    add_movie("Interstellar", "Christopher Nolan", 2014)

    list_movies()  # Выводим фильмы после добавления

    # Обновление фильма
    update_movie(1, "Inception", "Christopher Nolan", 2010)  # Изменим данные о фильме с ID 1
    update_movie(4, "Non-existing Movie", "Unknown", 2022)  # Попытаемся обновить несуществующий фильм

    # Удаление фильма
    delete_movie(2)  # Удаляем фильм с ID 2
    delete_movie(4)  # Попытаемся удалить несуществующий фильм

    list_movies()  # Выводим фильмы после удаления

    # Закрытие сессии
    session.close()
