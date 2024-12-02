from flask import Flask, render_template

app = Flask(__name__)

# Список книг для отображения
books = [
    {"title": "1984", "author": "Джордж Оруэлл"},
    {"title": "Мастер и Маргарита", "author": "Михаил Булгаков"},
    {"title": "Убить пересмешника", "author": "Харпер Ли"},
    {"title": "Гарри Поттер и философский камень", "author": "Джоан Роулинг"},
]

@app.route('/')
def home():
    return render_template('books.html', books=books)

if __name__ == '__main__':
    app.run(debug=True)
