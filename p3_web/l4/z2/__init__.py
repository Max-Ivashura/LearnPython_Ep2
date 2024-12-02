from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Список задач как временное хранилище
tasks = []
next_id = 1

# Получение списка задач
@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks), 200

# Добавление новой задачи
@app.route('/tasks', methods=['POST'])
def create_task():
    global next_id
    if not request.json or 'title' not in request.json:
        abort(400)  # Ошибка 400: Неверный запрос
    task = {
        'id': next_id,
        'title': request.json['title'],
        'completed': False
    }
    tasks.append(task)
    next_id += 1
    return jsonify(task), 201  # 201: Создано

# Получение задачи по ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404)  # Ошибка 404: Не найдено
    return jsonify(task), 200

# Обновление задачи
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404)
    if not request.json:
        abort(400)
    task['title'] = request.json.get('title', task['title'])
    task['completed'] = request.json.get('completed', task['completed'])
    return jsonify(task), 200

# Удаление задачи
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    task = next((task for task in tasks if task['id'] == task_id), None)
    if task is None:
        abort(404)
    tasks = [task for task in tasks if task['id'] != task_id]
    return jsonify({"result": True}), 204  # 204: Нет содержимого

# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
