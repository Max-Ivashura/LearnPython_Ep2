from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return '''
        <form method="POST" action="/greet">
            <input type="text" name="name" placeholder="Введите ваше имя">
            <input type="submit" value="Отправить">
        </form>
    '''


@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']  # Получаем имя из формы
    return f'Привет, {name}!'  # Отображаем приветственное сообщение


if __name__ == '__main__':
    app.run(debug=True)
