import os
import psycopg2
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
from flask import Flask, render_template, request, flash

def get_db_url():
    url = os.environ.get("DATABASE_URL")
    if url and url.startswith("postgres://"):
        url = url.replace("postgres://", "postgresql://", 1)
    if url and "sslmode" not in url:
        url += "?sslmode=require"
    return url


DB_URL = get_db_url()

def init_db():
    """Initializes the database."""
    try:
        conn = psycopg2.connect(DB_URL)
        with conn:
            with conn.cursor() as cur:
                # Create table with proper constraints
                cur.execute(
                    """
                    CREATE TABLE IF NOT EXISTS counter (
                        id INTEGER PRIMARY KEY,
                        count INTEGER NOT NULL DEFAULT 0
                    )
                    """
                )
                # Initialize the counter if it doesn't exist
                cur.execute(
                    """
                    INSERT INTO counter (id, count)
                    VALUES (1, 0)
                    ON CONFLICT (id) DO NOTHING
                    """
                )
        conn.close()
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

@app.route("/")
@app.route("/hello")
def index():
    flash("what's your name?")
    return render_template("index.html")

@app.route("/health")
def health():
    return {"status": "OK"}, 200

@app.route("/greet", methods=["POST", "GET"])
def greet():
    name = request.form.get("name_input", "").strip()
    if name:
        flash(f"Hi {name}, great to see you!")
    else:
        flash("Please enter your name.")

    try:
        conn = psycopg2.connect(DB_URL)
        with conn:
            with conn.cursor() as cur:
                cur.execute("UPDATE counter SET count = count + 1 WHERE id = 1")
                cur.execute("SELECT count FROM counter WHERE id = 1")
                count = cur.fetchone()[0]
        conn.close()
    except Exception as e:
        print(f"Database error: {str(e)}")
        count = 0

    return render_template("index.html", greeting_count=count)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)