from flask import Flask, jsonify

# Создайте экземпляр Flask
app = Flask(__name__)

# Создайте конечную точку для /, которая возвращает JSON
@app.route('/', methods=['GET'])
def hello_world():
    return jsonify(message="Hello, World!")

# Запустите приложение
if __name__ == "__main__":
    app.run(debug=True)
