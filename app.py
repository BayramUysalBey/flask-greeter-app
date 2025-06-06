import os
import sqlite3
import sys
import gunicorn
from flask import Flask, render_template, request, flash, g


app = Flask(__name__)
app.secret_key = "jfh_dgkhgjdjf"

@app.route('/')
def home():
    return "Flask Greeter is running! Go to /hello"

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

    # Update counter  
    db = get_db()  
    db.execute('UPDATE counter SET count = count + 1 WHERE id = 1')  
    db.commit()  

    # Get current count  
    count = db.execute('SELECT count FROM counter WHERE id = 1').fetchone()[0]  

    return render_template('index.html', greeting_count=count)  # Pass to template  

if sys.platform == "win32":
    from gevent import monkey
    monkey.patch_all()
	

DATABASE = 'greetings.db'  

def get_db():  
    db = getattr(g, '_database', None)  
    if db is None:  
        db = g._database = sqlite3.connect(DATABASE)  
        # Create table if not exists  
        db.execute('''CREATE TABLE IF NOT EXISTS counter  
                      (id INTEGER PRIMARY KEY, count INTEGER)''')  
        db.execute('INSERT OR IGNORE INTO counter (id, count) VALUES (1, 0)')  
    return db  

@app.teardown_appcontext  
def close_db(exception):  
    db = getattr(g, '_database', None)  
    if db is not None:  
        db.close()
        
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)