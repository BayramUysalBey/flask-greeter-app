import os
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from flask import Flask, render_template, request, flash


def get_db_url():
    url = os.environ.get("DATABASE_URL")  # from Render
    if not url:
        # fallback for local dev
        url = "postgresql://greeter_vnlr_user:vNOMTE9yY8qCobJF9JTGJN7QxdkCgBHa@dpg-d3hq54m3jp1c73foilv0-a/greeter_vnlr"
    # Normalize scheme for SQLAlchemy/psycopg2 consistency
    if url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    # Ensure sslmode=require in production (Render)
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    if "sslmode" not in query:
        query["sslmode"] = ["require"]
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))

DB_URL = get_db_url()

import psycopg2

def init_db():
    try:
        conn = psycopg2.connect(DB_URL)
        with conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS counter (
                        id INTEGER PRIMARY KEY,
                        count INTEGER NOT NULL DEFAULT 0
                    )
                """)
                cur.execute("""
                    INSERT INTO counter (id, count)
                    VALUES (1, 0)
                    ON CONFLICT (id) DO NOTHING
                """)
        conn.close()
    except Exception as e:
        print(f"Database initialization error: {str(e)}")
        raise



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
	count = 0
    try: 
        conn = psycopg2.connect(DB_URL) 
        with conn: 
            with conn.cursor() as cur: 
                # Update the counter
                cur.execute('UPDATE counter SET count = count + 1 WHERE id = 1') 
                # Get the updated count
                cur.execute('SELECT count FROM counter WHERE id = 1') 
                count = cur.fetchone()[0] 
        conn.close()
    except Exception as e: 
        print(f"Database error: {str(e)}") 
        # Count will remain 0 if there's an error
    
    return render_template('index.html', greeting_count=count)

if __name__ == "__main__":
    # Initialize the database before starting the app
    init_db()
    
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)