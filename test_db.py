# test_db.py
import os
from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
import psycopg2

def get_db_url(): 
    url = os.environ.get("DATABASE_URL") 
    if not url: 
        return "postgresql://postgres:password@localhost:5432/greeter"
    
    parsed = urlparse(url)
    query = parse_qs(parsed.query)
    
    if "sslmode" not in query:
        query["sslmode"] = ["require"]
    
    new_query = urlencode(query, doseq=True)
    return urlunparse(parsed._replace(query=new_query))

DB_URL = get_db_url()

try:
    conn = psycopg2.connect(DB_URL)
    print("✅ Successfully connected to database!")
    conn.close()
except Exception as e:
    print(f"❌ Database connection failed: {str(e)}")