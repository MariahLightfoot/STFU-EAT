from flask import Flask, render_template
from sqlite import create_table, data_entry
from Restaurant import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    return render_template('result.html')

# if __name__ == '__main__':
#     app.run(debug=True)

lonas = Restaurant("Lonas LiL Eats", "/static/images/lonas-lil-eats.jpg") 
lonas1 = Restaurant("Lonas LiL Eats", "/static/images/lonas-lil-eats.jpg") 
# insertStatement = '"INSERT INTO local_stl_restaurants VALUES(?,?,?)", (lonas.id, lonas.name, lonas.image)'
    # c.execute("INSERT INTO local_stl_restaurants VALUES(1, 'Lonas LiL Eats', '/static/images/lonas-lil-eats.jpg')")

create_table()
# data_entry(insertStatement)
print(lonas.id)
print(lonas1.id)
