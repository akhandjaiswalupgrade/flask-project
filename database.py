from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def add_user():
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
    cur.execute("INSERT INTO users (name) VALUES (?)", ("Shiv",))
    conn.commit()
    conn.close()
    return "User added successfully!"

if __name__ == '__main__':
    app.run(debug=True)
