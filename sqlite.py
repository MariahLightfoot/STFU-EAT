import sqlite3

conn = sqlite3.connect('STFUEAT.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS local_stl_restaurants(id INT, name TEXT, image TEXT)')

def data_entry():
    c.execute("INSERT INTO local_stl_restaurants VALUES(1, 'Lonas LiL Eats', '/static/images/lonas-lil-eats.jpg')")
    c.execute("INSERT INTO local_stl_restaurants VALUES(2, 'Mochi Cafe', '/static/images/mochi-cafe.jpg')")
    c.execute("INSERT INTO local_stl_restaurants VALUES(4, 'VP Square', '/static/images/vp-sqaure.jpg')")
    c.execute("INSERT INTO local_stl_restaurants VALUES(3, 'Southwest Market', '/static/images/southwest-market.jpg')")
    c.execute("INSERT INTO local_stl_restaurants VALUES(5, 'Copper Pig', '/static/images/copper-pig.jpg')")
    conn.commit()

create_table()
data_entry()

c.execute("SELECT * FROM local_stl_restaurants WHERE name='Lonas LiL Eats'")
print(c.fetchone())

