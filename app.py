from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
app.secret_key = 'super-secret-key-for-variant-3'

USERS = {
    'admin': 'secret123',
    'arseniy': 'student2026'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def show_data():
    courses = [
        {'title': 'Flask Web Dev', 'level': 'Базовый', 'hours': 36, 'description': 'Маршрутизация, шаблонизация Jinja2, сессии.'},
        {'title': 'FastAPI REST API', 'level': 'Продвинутый', 'hours': 48, 'description': 'Асинхронные эндпоинты, Pydantic схемы, Swagger UI.'},
        {'title': 'Базы данных и ORM', 'level': 'Средний', 'hours': 40, 'description': 'Работа с SQLite, PostgreSQL и SQLAlchemy.'}
    ]
    return render_template('data.html', courses=courses)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()
        if username in USERS and USERS[username] == password:
            session['user'] = username
            flash('Успешный вход в систему!', 'success')
            return redirect(url_for('dashboard'))
        flash('Неверное имя пользователя или пароль.', 'danger')
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    if 'user' not in session:
        flash('Пожалуйста, авторизуйтесь для доступа к кабинету.', 'warning')
        return redirect(url_for('login'))
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash('Вы вышли из учетной записи.', 'info')
    return redirect(url_for('index'))

@app.route('/health')
def health_check():
    return {'status': 'ok', 'variant': '3'}, 200

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
