from db_config import get_connection

try:
    conn = get_connection()
    print("✅ Database connection successful!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:", e)

