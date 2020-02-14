import sqlite3

conn = sqlite3.connect('STFUEAT.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS local_stl_restuarants(id INT, name TEXT, image BLOB)')

def data_entry():
    c.execute("INSERT INTO local_stl_restuarants VALUES(1, 'Lonas LiL Eats', 'lonas-lil-eats.jpg')")
    c.execute("INSERT INTO local_stl_restuarants VALUES(2, 'Mochi Cafe', 'mochi-cafe.jpg')")
    c.execute("INSERT INTO local_stl_restuarants VALUES(4, 'VP Square', 'vp-sqaure.jpg')")
    c.execute("INSERT INTO local_stl_restuarants VALUES(3, 'Southwest Market', 'southwest-market.jpg')")
    c.execute("INSERT INTO local_stl_restuarants VALUES(5, 'Copper Pig', 'copper-pig.jpg')")
    conn.commit()
    c.close()
    conn.close()

create_table()
data_entry()
