import sqlite3

conn = sqlite3.connect('STFU-EAT.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS local_stl_restuarants(id INT, name TEXT)')

def data_entry():
    c.execute("INSERT INTO local_stl_restuarants VALUES(1, 'Lonas LiL Eats')")
    c.execute("INSERT INTO local_stl_restuarants VALUES(2, 'Mochi Cafe')")
    c.execute("INSERT INTO local_stl_restuarants VALUES(3, 'Southwest Market')")
    c.execute("INSERT INTO local_stl_restuarants VALUES(4, 'Macs Local Eats')")
    c.execute("INSERT INTO local_stl_restuarants VALUES(5, 'Copper Pig')")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
