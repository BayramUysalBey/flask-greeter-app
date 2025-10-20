#!/bin/sh
set -e

# --- 1. WAIT FOR DATABASE CONNECTION ---

python -c "
import socket; 
import time; 

while True: 
    try: 
        s = socket.create_connection(('db', 5432), timeout=5)
        s.close()
        break
    except socket.error: 
        time.sleep(1)
"

# --- 2. INITIALIZE TABLES ---

python -c "from app import create_tables; create_tables()"

# --- 3. START WEB SERVER ---

exec gunicorn -b :5000 --access-logfile - --error-logfile - app:app
