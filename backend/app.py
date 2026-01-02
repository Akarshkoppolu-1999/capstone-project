from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
import os
import time

app = Flask(__name__)
CORS(app)

# Database connection configuration
DB_HOST = os.getenv('DB_HOST', 'db')
DB_NAME = os.getenv('DB_NAME', 'capstone_db')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASS = os.getenv('DB_PASS', 'postgres')

def get_db_connection():
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                database=DB_NAME,
                user=DB_USER,
                password=DB_PASS
            )
            return conn
        except Exception as e:
            print(f"Error connecting to database: {e}. Retrying in 5 seconds...")
            time.sleep(5)

@app.route('/')
def hello():
    return jsonify({"message": "Welcome to the Capstone Project API!", "status": "success"})

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

@app.route('/api/init')
def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS visitors (id serial PRIMARY KEY, visit_time timestamp DEFAULT CURRENT_TIMESTAMP);')
    cur.execute('INSERT INTO visitors DEFAULT VALUES;')
    conn.commit()
    cur.execute('SELECT COUNT(*) FROM visitors;')
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return jsonify({"message": "Database initialized!", "visit_count": count})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
