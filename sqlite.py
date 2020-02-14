import sqlite3

conn = sqlite3.connect('STFU-EAT.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS local_stl_restuarants(id INT, name TEXT)')

def data_entry():
    c.execute("INSERT INTO local_stl_restuarants VALUES(1, 'hello')")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
