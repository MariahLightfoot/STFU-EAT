import random
from flask import Flask, render_template, request
from sqlite import create_table, data_entry, pull_img_from_db
from Restaurant import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)

# create_table()

lonasLilEats = Restaurant("Lonas LiL Eats", "/static/images/lonas-lil-eats.jpg") 
vpSqaure = Restaurant("VP Square", "/static/images/vp-sqaure.jpg")
copperPig = Restaurant("Copper Pig", "/static/images/copper-pig.jpg")
mochiCafe = Restaurant("Mochi Cafe", "/static/images/mochi-cafe.jpg")
# southwestMarket = Restaurant("Southwest Market", "southwest-market.jpg")

# data_entry(mochiCafe)

restaurantChoices = [lonasLilEats, vpSqaure, copperPig, mochiCafe]

def randomRestaurantSelection():
    value = random.randint(0, len(restaurantChoices)-1)
    print(value)
    return restaurantChoices[value]

name = randomRestaurantSelection().name
image = pull_img_from_db(name)[0]

@app.route('/result')
def result():
    return render_template('result.html', name=name, image=image)
