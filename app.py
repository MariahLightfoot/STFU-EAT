from flask import Flask, render_template
from sqlite import create_table, data_entry, pull_img_from_db
from Restaurant import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# create_table()

lonas = Restaurant("Lonas LiL Eats", "/static/images/lonas-lil-eats.jpg") 
# vpSqaure = Restaurant("VP Square", "vp-sqaure.jpg")
# copperPig = Restaurant("Copper Pig", "copper-pig.jpg")
# mochiCafe = Restaurant("Mochi Cafe", "mochi-cafe.jpg")
# southwestMarket = Restaurant("Southwest Market", "southwest-market.jpg")

# data_entry(lonas)

name = "Lonas LiL Eats"
image = pull_img_from_db(lonas)[0]

@app.route('/result')
def result():
    return render_template('result.html', name=name, image=image)

#thinking i can create objects, store them in array
#random function will choose restaurant
#can display name that way
#look in db for img
