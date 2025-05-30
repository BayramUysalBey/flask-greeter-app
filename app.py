import sqlite3  
from flask import Flask, render_template, request, flash, g


app = Flask(__name__)
app.secret_key = "jfh_dgkhgjdjf"

@app.route("/hello")
def index():
	flash("what's your name?")
	return render_template("index.html")

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