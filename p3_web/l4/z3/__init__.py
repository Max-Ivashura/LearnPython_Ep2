from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Настройка базы данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Определение модели задачи
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=True)
    completed = db.Column(db.Boolean, default=False)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed
        }

with app.app_context():
    db.create_all()


# Получение списка задач
@app.route('/tasks', methods=['GET'])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200


# Добавление новой задачи
@app.route('/tasks', methods=['POST'])
def create_task():
    if not request.json or 'title' not in request.json:
        abort(400)

    task = Task(
        title=request.json['title'],
        description=request.json.get('description'),
        completed=request.json.get('completed', False)
    )
    db.session.add(task)
    db.session.commit()
    return jsonify(task.to_dict()), 201


# Получение задачи по ID
@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        abort(404)
    return jsonify(task.to_dict()), 200


# Обновление задачи
@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        abort(404)

    if not request.json:
        abort(400)

    task.title = request.json.get('title', task.title)
    task.description = request.json.get('description', task.description)
    task.completed = request.json.get('completed', task.completed)

    db.session.commit()
    return jsonify(task.to_dict()), 200


# Удаление задачи
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        abort(404)

    db.session.delete(task)
    db.session.commit()
    return jsonify({"result": True}), 204


# Запуск приложения
if __name__ == '__main__':
    app.run(debug=True)
