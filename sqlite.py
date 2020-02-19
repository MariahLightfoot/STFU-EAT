import sqlite3

conn = sqlite3.connect('STFUEAT.db')
c = conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS local_stl_restaurants(id INT, name TEXT, image TEXT, moreInfo TEXT)')

def data_entry(restaurantObject):
    id = restaurantObject.id
    name = restaurantObject.name
    image = restaurantObject.image
    moreInfo = restaurantObject.moreInfo
    c.execute("INSERT INTO local_stl_restaurants (id, name, image, moreInfo) VALUES(?, ?, ?, ?)",
                (id, name, image, moreInfo))
    conn.commit()

def pull_img_from_db(restaurantName):
    c.execute('SELECT image FROM local_stl_restaurants WHERE name=?', (restaurantName,))
    data = c.fetchone()
    return data

def pull_moreInfo_from_db(restaurantName):
    c.execute('SELECT moreInfo FROM local_stl_restaurants WHERE name=?', (restaurantName,))
    data = c.fetchone()
    return data
    

