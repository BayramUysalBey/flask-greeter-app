import os
import psycopg2
from flask import Flask, render_template, request, flash

# Database configuration
DB_NAME = os.environ.get("DB_NAME", "greeter")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASS = os.environ.get("DB_PASS", "password")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_PORT = os.environ.get("DB_PORT", "5432")

def init_db():
    """Initializes the database."""
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, 
            user=DB_USER, 
            password=DB_PASS, 
            host=DB_HOST, 
            port=DB_PORT
        )
        with conn:
            with conn.cursor() as cur:
                # Create table with proper constraints
                cur.execute('''
                    CREATE TABLE IF NOT EXISTS counter (
                        id INTEGER PRIMARY KEY,
                        count INTEGER NOT NULL DEFAULT 0
                    )
                ''')
                
                # Initialize the counter if it doesn't exist
                cur.execute("""
                    INSERT INTO counter (id, count) 
                    VALUES (1, 0)
                    ON CONFLICT (id) DO NOTHING
                """)
    except Exception as e:
        print(f"Database initialization error: {str(e)}")
        raise
# Initialize database
try:
    init_db()
except Exception as e:
    print(f"Failed to initialize database: {str(e)}")

app = Flask(__name__)
app.secret_key = "jfh_dgkhgjdjf"

@app.route('/')
# def home():
#     return "Flask Greeter is running! Go to /hello"
@app.route("/hello")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route('/health')
def health():
    return {"status": "OK"}, 200

@app.route('/greet', methods=['POST', 'GET'])  
def greet():  
    name = request.form['name_input']  
    flash(f"Hi {name}, great to see you!")  
    
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME, 
            user=DB_USER, 
            password=DB_PASS, 
            host=DB_HOST, 
            port=DB_PORT
        )
        with conn:
            with conn.cursor() as cur:
                cur.execute('UPDATE counter SET count = count + 1 WHERE id = 1')
                cur.execute('SELECT count FROM counter WHERE id = 1')
                count = cur.fetchone()[0]
        conn.close()
    except Exception as e:
        print(f"Database error: {str(e)}")
        count = 0
    
    return render_template('index.html', greeting_count=count)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)