import sqlite3

conn = sqlite3.connect('STFUEAT.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS local_stl_restaurants(id INT, name TEXT, image TEXT, directions TEXT)')

def data_entry(restaurantObject):
    id = restaurantObject.id
    name = restaurantObject.name
    image = restaurantObject.image
    directions = restaurantObject.directions
    c.execute("INSERT INTO local_stl_restaurants (id, name, image, directions) VALUES(?, ?, ?, ?)",
                (id, name, image, directions))
    conn.commit()

def pull_img_from_db(restaurantName):
    c.execute('SELECT image FROM local_stl_restaurants WHERE name=?', (restaurantName,))
    data = c.fetchone()
    return data

def pull_directions_from_db(restaurantName):
    c.execute('SELECT directions FROM local_stl_restaurants WHERE name=?', (restaurantName,))
    data = c.fetchone()
    return data
    

