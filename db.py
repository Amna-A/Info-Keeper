import sqlite3

class Database():
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS students (id INTEGER PRIMARY KEY, name text,grade text) ")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM students")
        rows = self.cur.fetchall()
        return rows

    def insert(self, name, grade):
        self.cur.execute("INSERT INTO students VALUES (NULL, ?,?)", (name, grade))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM students WHERE id=?", (id,))
        self.conn.commit()

    def update(self,name, grade,id):
        self.cur.execute("UPDATE students SET name = ?, grade = ? WHERE id = ?", (name,grade,id))
        self.conn.commit()
        

    def __del__(self):
        self.conn.close()

db = Database('student-data.db')
