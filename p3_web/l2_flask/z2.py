from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Добро пожаловать на главную страницу!'


@app.route('/about')
def about():
    return 'Информация обо всем: Максим, 23 года, пытаюсь разобраться во Flask, люблю программирование и путешествия.'


if __name__ == '__main__':
    app.run(debug=True)