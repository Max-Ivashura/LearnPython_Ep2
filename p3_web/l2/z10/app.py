from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Хранение задач в памяти
tasks = []


@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:  # Проверяем, что задача не пустая
        tasks.append(task)  # Добавление задачи в список
    return jsonify(tasks)  # Возвращаем обновленный список задач в формате JSON


# Обработка ошибок 404
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


# Обработка ошибок 500
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run(debug=True)
