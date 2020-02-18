import random
from flask import Flask, render_template, request
from sqlite import create_table, data_entry, pull_img_from_db, pull_directions_from_db
from Restaurant import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# create_table()

lonasLilEats = Restaurant("Lonas LiL Eats", "/static/images/lonas-lil-eats.jpg", "https://www.google.com/maps/dir/Capacity,+Delmar+Boulevard+Suite+300,+University+City,+MO/lonas+lil+eats/@38.6336436,-90.3040077,13z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x87d8caecf081d9dd:0xfdf024901c97f03a!2m2!1d-90.307561!2d38.656469!1m5!1m1!1s0x87d8b47fccee2a1d:0xa12a5a4a22fc4d33!2m2!1d-90.2267431!2d38.6102103") 
vpSqaure = Restaurant("VP Square", "/static/images/vp-sqaure.jpg", "https://www.google.com/maps/dir/Capacity,+Delmar+Boulevard+Suite+300,+University+City,+MO/VP+Square,+Juniata+Street,+St.+Louis,+MO/@38.6288414,-90.3097068,13z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x87d8caecf081d9dd:0xfdf024901c97f03a!2m2!1d-90.307561!2d38.656469!1m5!1m1!1s0x87d8b467f769872b:0x1463b550668e05dc!2m2!1d-90.242984!2d38.601137")
copperPig = Restaurant("Copper Pig", "/static/images/copper-pig.jpg", "https://www.google.com/maps/dir/Capacity,+Delmar+Boulevard+Suite+300,+University+City,+MO/Copper+Pig,+Macklind+Avenue,+St.+Louis,+MO/@38.6217144,-90.327216,13z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x87d8caecf081d9dd:0xfdf024901c97f03a!2m2!1d-90.307561!2d38.656469!1m5!1m1!1s0x87d8b5eb733f66c1:0x9ed721301182d9c0!2m2!1d-90.2843284!2d38.5874652")
mochiCafe = Restaurant("Mochi Cafe", "/static/images/mochi-cafe.jpg", "https://www.google.com/maps/dir/Capacity,+Delmar+Boulevard+Suite+300,+University+City,+MO/Cafe+Mochi,+3221+S+Grand+Blvd+%231013,+St.+Louis,+MO+63118/@38.6277875,-90.3097068,13z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x87d8caecf081d9dd:0xfdf024901c97f03a!2m2!1d-90.307561!2d38.656469!1m5!1m1!1s0x87d8b46826f982bb:0xcbda860045e509fd!2m2!1d-90.2431011!2d38.5985033")
# southwestMarket = Restaurant("Southwest Market", "southwest-market.jpg", "https://www.google.com/maps/dir/Capacity,+Delmar+Boulevard+Suite+300,+University+City,+MO/Southwest+Market+Cuisine,+Columbia+Avenue,+St.+Louis,+MO/@38.6339779,-90.327216,13z/data=!3m1!4b1!4m13!4m12!1m5!1m1!1s0x87d8caecf081d9dd:0xfdf024901c97f03a!2m2!1d-90.307561!2d38.656469!1m5!1m1!1s0x87d8b509de349b7d:0xfa960b104bf9d77!2m2!1d-90.2749085!2d38.6108659")

# data_entry(mochiCafe)

restaurantChoices = [lonasLilEats, vpSqaure, copperPig, mochiCafe]

def randomRestaurantSelection():
    value = random.randint(0, len(restaurantChoices)-1)
    return restaurantChoices[value]

name = randomRestaurantSelection().name
image = pull_img_from_db(name)[0]
directions = pull_directions_from_db(name)[0]

@app.route('/result')
def result():
    return render_template('result.html', name=name, image=image, directions=directions)
