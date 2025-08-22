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

### Screenshots
![demo1
](<Screenshot 2025-07-19 154157 - Copy.png>) ![demo2
](<Screenshot 2025-07-19 154236.png>) ![demo3
](<Screenshot 2025-07-19 154254.png>) ![demo4
](<Screenshot 2025-07-21 113207.png>) ![demo5
](<Screenshot 2024-07-24 152714.png>)
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
