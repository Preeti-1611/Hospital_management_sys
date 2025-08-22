from flask import Flask, render_template, request, redirect, url_for, jsonify, session, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from db_config import get_connection
import os

app = Flask(__name__)
app.secret_key = os.urandom(24)  # Generate a random secret key

# Initialize Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# User model
class User(UserMixin):
    def __init__(self, id, username, role):
        self.id = id
        self.username = username
        self.role = role

@login_manager.user_loader
def load_user(user_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user_data = cursor.fetchone()
    conn.close()
    
    if user_data:
        return User(user_data['id'], user_data['username'], user_data['role'])
    return None

# Create users table if it doesn't exist
def create_users_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            role VARCHAR(20) NOT NULL DEFAULT 'user',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    
    # Insert default admin user if not exists
    cursor.execute("SELECT * FROM users WHERE username = 'admin'")
    if not cursor.fetchone():
        admin_password = generate_password_hash('admin123')
        cursor.execute("""
            INSERT INTO users (username, password_hash, role) 
            VALUES ('admin', %s, 'admin')
        """, (admin_password,))
    
    conn.commit()
    conn.close()

# Initialize database
create_users_table()

# Route: Home Page
@app.route('/')
def home():
    return render_template('index.html')

# Route: Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        user_data = cursor.fetchone()
        conn.close()
        
        if user_data and check_password_hash(user_data['password_hash'], password):
            user = User(user_data['id'], user_data['username'], user_data['role'])
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'error')
    
    return render_template('login.html')

# Route: Logout
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out', 'info')
    return redirect(url_for('home'))

# Route: Dashboard (protected)
@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('index.html')

# Route: Doctor List (protected)
@app.route('/doctors')
@login_required
def show_doctors():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM doctor")
    doctors = cursor.fetchall()
    conn.close()
    return render_template('doctor.html', doctors=doctors)

# Route: Nurse List with Shift Filter (protected)
@app.route('/nurses')
@login_required
def show_nurses():
    shift = request.args.get('shift', '')  # get shift from dropdown
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    if shift:
        cursor.execute("SELECT * FROM nurse WHERE shift = %s", (shift,))
    else:
        cursor.execute("SELECT * FROM nurse")
    nurses = cursor.fetchall()
    conn.close()
    return render_template('nurse.html', nurses=nurses)

@app.route('/patient.html')
@login_required
def patient():
    return render_template('patient.html')

@app.route('/doctor.html')
@login_required
def doctor():
    return render_template('doctor.html')

@app.route('/nurse.html')
@login_required
def nurse():
    return render_template('nurse.html')

@app.route('/appoi.html')
@login_required
def appoi():
    return render_template('appoi.html')

@app.route('/index.html')
@login_required
def index():
    return render_template('index.html')

@app.route('/appointment_list.html')
@login_required
def appointment_list():
    return render_template('appointement_list.html')

@app.route('/login.html')
def login_page():
    return render_template('login.html')

@app.route('/api/patients', methods=['POST'])
@login_required
def add_patient():
    data = request.get_json()
    conn = get_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO patient (patient_id, name, sex, age, dob, mobile, address, disease, join_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (
        data['patient_id'],
        data['name'],
        data['sex'],
        data['age'],
        data['dob'],
        data['mobile'],
        data['address'],
        data['disease'],
        data['join_date']
    ))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Patient added successfully'}), 201

@app.route('/api/patients', methods=['GET'])
@login_required
def get_patients():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM patient")
    patients = cursor.fetchall()
    conn.close()
    return jsonify(patients)

@app.route('/api/appointments', methods=['GET'])
@login_required
def get_appointments():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM appointment ORDER BY created_at DESC")
    appointments = cursor.fetchall()
    conn.close()
    return jsonify(appointments)

@app.route('/submit_appointment', methods=['POST'])
@login_required
def submit_appointment():
    try:
        name = request.form['name']
        sex = request.form['sex']
        age = request.form['age']
        dob = request.form['dob']
        mobile = request.form['mobile']
        address = request.form['address']
        
        conn = get_connection()
        cursor = conn.cursor()
        sql = """
            INSERT INTO appointment (name, sex, age, dob, mobile, address)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(sql, (name, sex, age, dob, mobile, address))
        conn.commit()
        conn.close()
        
        return "Appointment submitted successfully!", 200
    except Exception as e:
        return f"Error: {str(e)}", 500


if __name__ == '__main__':
    app.run(debug=True)
