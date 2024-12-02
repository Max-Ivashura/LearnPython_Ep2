from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Добро пожаловать на главную страницу!'


@app.route('/greet/<name>')
def show_user_profile(name):
    return f'Hello, {name}!'


if __name__ == '__main__':
    app.run(debug=True)
