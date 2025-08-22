# Nursing Management System

A comprehensive web-based Nursing Management System built with Flask and MySQL, featuring user authentication and session management.

## Features

- 🔐 **Secure Authentication**: User login/logout with session management
- 👥 **User Management**: Role-based access control
- 🏥 **Patient Management**: Add and view patient records
- 👨‍⚕️ **Doctor Management**: Manage doctor information
- 👩‍⚕️ **Nurse Management**: Track nurse assignments and shifts
- 📅 **Appointment System**: Book and manage appointments
- 💰 **Billing System**: Handle patient billing
- 📋 **Medical Records**: Maintain patient medical records

## Prerequisites

Before running this application, make sure you have:

1. **Python 3.7+** installed
2. **MySQL Server** installed and running
3. **MySQL Connector** for Python

## Installation

### 1. Clone the Repository
```bash
git clone <repository-url>
cd nursing-mgmt-sys
```

### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 3. Database Setup

#### Create MySQL Database
```sql
CREATE DATABASE system_nursing;
USE system_nursing;
```

#### Create Required Tables
The application will automatically create the `users` table on first run. For other tables, you'll need to create them based on your specific requirements.

### 4. Configure Database Connection

Edit `backend/db_config.py` with your MySQL credentials:

```python
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="your_username",          # Update this
        password="your_password",      # Update this
        database="system_nursing"
    )
```

## Running the Application

### 1. Start the Flask Server
```bash
cd backend
python app.py
```

### 2. Access the Application
Open your web browser and navigate to:
```
http://localhost:5000
```

### 3. Login
Use the default credentials:
- **Username**: `admin`
- **Password**: `admin123`

## Project Structure

```
nursing-mgmt-sys/
├── backend/
│   ├── app.py              # Main Flask application
│   ├── db_config.py        # Database configuration
│   └── templates/          # HTML templates
│       ├── index.html      # Home page
│       ├── login.html      # Login page
│       ├── patient.html    # Patient management
│       ├── doctor.html     # Doctor management
│       ├── nurse.html      # Nurse management
│       └── appoi.html      # Appointment booking
├── requirements.txt        # Python dependencies
└── README.md             # This file
```

## Authentication System

The application uses Flask-Login for secure authentication:

- **Session Management**: Secure user sessions with random secret keys
- **Password Hashing**: Passwords are securely hashed using Werkzeug
- **Protected Routes**: All sensitive pages require authentication
- **User Roles**: Support for different user roles (admin, user)

## Default Admin Account

The system automatically creates a default admin account:
- Username: `admin`
- Password: `admin123`

**Important**: Change these credentials in production!

## API Endpoints

### Protected Endpoints (require login)
- `GET /dashboard` - Main dashboard
- `GET /doctors` - View doctors
- `GET /nurses` - View nurses
- `GET /patient.html` - Patient management
- `POST /api/patients` - Add new patient
- `GET /api/patients` - Get all patients
- `GET /api/appointments` - Get appointments
- `POST /submit_appointment` - Submit appointment

### Public Endpoints
- `GET /` - Public home page
- `GET /login` - Login page
- `POST /login` - Login authentication
- `GET /logout` - Logout (requires login)


### Common Issues

1. **Database Connection Error**
   - Verify MySQL is running
   - Check database credentials in `db_config.py`
   - Ensure database `system_nursing` exists

2. **Import Errors**
   - Run `pip install -r requirements.txt`
   - Check Python version (3.7+ required)

3. **Port Already in Use**
   - Change port in `app.py`: `app.run(debug=True, port=5001)`

4. **Template Not Found**
   - Ensure you're running from the `backend` directory
   - Check file paths in templates

### Development Mode

For development, the application runs in debug mode:
```python
app.run(debug=True)
```

This enables:
- Auto-reload on code changes
- Detailed error messages
- Debug toolbar

## Production Deployment

For production deployment:

1. **Disable Debug Mode**
   ```python
   app.run(debug=False)
   ```

2. **Use Production WSGI Server**
   ```bash
   pip install gunicorn
   gunicorn -w 4 -b 0.0.0.0:5000 app:app
   ```

3. **Set Environment Variables**
   ```bash
   export FLASK_ENV=production
   export SECRET_KEY=your-secret-key
   ```

4. **Configure Reverse Proxy** (Nginx/Apache)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License.

## Support

For support and questions:
- Create an issue in the repository
- Contact the development team

---

**Note**: This is a development version. For production use, ensure proper security measures are implemented. 
