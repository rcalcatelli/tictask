# app.py
from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SECRET_KEY'] = 'your_secret_key'  # Cambia esto a una clave secreta real
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    priority = db.Column(db.String(10), nullable=False)
    completed = db.Column(db.Boolean, default=False)
    order = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # Relación con el usuario

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    filter_option = request.args.get('filter', 'all')
    if filter_option == 'completed':
        tasks = Task.query.filter_by(completed=True).all()
    elif filter_option == 'not_completed':
        tasks = Task.query.filter_by(completed=False).all()
    else:
        tasks = Task.query.all()  # Mostrar todas las tareas
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    task_content = request.form.get('content')
    task_description = request.form.get('description')
    task_priority = request.form.get('priority')
    
    if task_content:  # Asegurarse de que el contenido no esté vacío
        new_task = Task(content=task_content, description=task_description, priority=task_priority, completed=False)
        db.session.add(new_task)
        db.session.commit()
    
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        task.completed = not task.completed  # Cambiar el estado de completado
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:task_id>', methods=['GET', 'POST'])
def edit_task(task_id):
    task = Task.query.get(task_id)
    if request.method == 'POST':
        task.content = request.form.get('content')
        task.description = request.form.get('description')
        task.priority = request.form.get('priority')
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('edit.html', task=task)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Crea la base de datos si no existe
    app.run(debug=True)