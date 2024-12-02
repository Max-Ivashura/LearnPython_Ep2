from flask import Flask, jsonify, request
import json
import os

app = Flask(__name__)
save_path = 'files/items.json'

# Функция для загрузки данных из файла items.json
def load_items():
    if os.path.exists(save_path):
        with open(save_path, 'r', encoding='cp1251') as f:
            return json.load(f)
    return []

# Функция для сохранения данных в файл items.json
def save_items():
    with open(save_path, 'w', encoding='cp1251') as f:
        json.dump(items, f, ensure_ascii=False)  # ensure_ascii=False для корректной записи данных в CP1251

# Список для хранения товаров, загружаем из файла
items = load_items()

# Конечная точка GET /items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items), 200

# Конечная точка POST /items
@app.route('/items', methods=['POST'])
def add_item():
    new_item = request.get_json()

    # Проверка на наличие обязательных полей
    if not new_item or 'name' not in new_item:
        return jsonify({'error': 'Bad request, name is required.'}), 400

    items.append(new_item)
    save_items()  # Сохраняем данные в файл
    return jsonify(new_item), 201

if __name__ == '__main__':
    app.run(debug=True)
