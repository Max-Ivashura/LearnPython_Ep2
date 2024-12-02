from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    user_name = "Максим"  # Пример переменной для условного рендеринга
    return render_template('index.html', name=user_name)

@app.route('/about')
def about():
    show_details = True  # Переменная, определяющая, показывать ли дополнительные детали
    return render_template('about.html', show_details=show_details)

if __name__ == '__main__':
    app.run(debug=True)
