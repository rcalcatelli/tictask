# TICTASK  
#### Video Demo: <URL HERE>

# Task Management Project in Flask - TICTASK

This is a task management project developed with Flask, which allows users to register, log in, and efficiently manage their tasks. Users can add, edit, delete, and mark tasks as completed. Additionally, the authentication system ensures that each user has their own task list.  

## Features  

- User registration  
- Login and session management  
- Add, edit, and delete tasks  
- Mark tasks as completed  
- Filter tasks by status (completed/incomplete)  
- Sort tasks  
- Responsive user interface  

## Technologies Used  

- **Flask**: Web framework for Python  
- **Flask-SQLAlchemy**: ORM for database management  
- **Flask-Login**: User session management  
- **Flask-WTF**: Form handling  
- **SQLite**: Lightweight database  
- **Bootstrap**: CSS framework for responsive design  

## Requirements  

- Python 3.x  
- pip (Python package manager)  

1. **Clone the repository**:  
   ```bash  
   git clone https://github.com/your_username/todo-app.git  
   cd todo-app  
   ```

2. **Create a virtual environment** (optional but recommended):  
   ```bash  
   python -m venv venv  
   source venv/bin/activate  # On Linux/Mac  
   venv\Scripts\activate  # On Windows  
   ```

3. **Install the dependencies**:  
   ```bash  
   pip install -r requirements.txt  
   ```

4. **Set up the database**:  
   - If you're using migrations, initialize the database:  
     ```bash  
     flask db init  
     flask db migrate -m "Initial migration."  
     flask db upgrade  
     ```

5. **Run the application**:  
   ```bash  
   python app.py  
   ```

6. **Access the application**:  
   - Open your browser and go to `http://127.0.0.1:5000/`.

## Usage  

- **Registration**: New users can register on the registration page.  
- **Login**: Users can log in with their credentials.  
- **Task Management**: Users can add new tasks, edit them, delete them, and mark them as completed.  

## Contributions  

Contributions are welcome. If you'd like to contribute, please follow these steps:

1. Fork the repository.  
2. Create a new branch (`git checkout -b feature/new-feature`).  
3. Make your changes and commit (`git commit -m 'Add new feature'`).  
4. Push the branch (`git push origin feature/new-feature`).  
5. Open a Pull Request.  

## Contact  

If you have any questions or suggestions, feel free to contact me at [rcalcatelli@gmail.com](mailto:rcalcatelli@gmail.com).
