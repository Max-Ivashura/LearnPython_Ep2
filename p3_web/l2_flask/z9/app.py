from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Хранение задач в памяти (для простоты)
tasks = []


@app.route('/')
def home():
    return render_template('index.html', tasks=tasks)


@app.route('/add_task', methods=['POST'])
def add_task():
    task = request.form.get('task')
    if task:  # Проверка, что задача не пустая
        tasks.append(task)
    return jsonify(tasks)


if __name__ == '__main__':
    app.run(debug=True)
