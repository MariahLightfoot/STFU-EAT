import sqlite3

conn = sqlite3.connect('STFUEAT.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS local_stl_restaurants(id INT, name TEXT, image TEXT)')

def data_entry(restaurantObject):
    id = restaurantObject.id
    name = restaurantObject.name
    image = restaurantObject.image
    c.execute("INSERT INTO local_stl_restaurants (id, name, image) VALUES(?, ?, ?)",
                (id, name, image))
    conn.commit()

def read_from_db():
    c.execute('SELECT * FROM local_stl_restaurants')
    data = c.fetchall()
    print(data)

