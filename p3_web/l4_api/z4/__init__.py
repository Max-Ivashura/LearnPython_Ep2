from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

# Настройка базы данных SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Секретный ключ для JWT
db = SQLAlchemy(app)
jwt = JWTManager(app)


# Определение модели пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


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


# Создание базы данных
with app.app_context():
    db.create_all()


# Регистрация пользователя
@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    if User.query.filter_by(username=username).first():
        return jsonify({"msg": "User already exists"}), 400

    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User registered successfully"}), 201


# Вход в систему
@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()

    if user and check_password_hash(user.password, password):
        # Создание токена
        access_token = create_access_token(identity={'username': user.username})
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Bad username or password"}), 401


# Получение списка задач (защищенный маршрут)
@app.route('/tasks', methods=['GET'])
@jwt_required()
def get_tasks():
    tasks = Task.query.all()
    return jsonify([task.to_dict() for task in tasks]), 200


# Добавление новой задачи (защищенный маршрут)
@app.route('/tasks', methods=['POST'])
@jwt_required()
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

# Получение задачи по ID (защищенный маршрут)
@app.route('/tasks/<int:task_id>', methods=['GET'])
@jwt_required()
def get_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        abort(404)
    return jsonify(task.to_dict()), 200

# Обновление задачи (защищенный маршрут)
@app.route('/tasks/<int:task_id>', methods=['PUT'])
@jwt_required()
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

# Удаление задачи (защищенный маршрут)
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
@jwt_required()
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
