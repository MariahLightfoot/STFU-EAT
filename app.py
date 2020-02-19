import random
from flask import Flask, render_template, request
from sqlite import create_table, data_entry, pull_img_from_db, pull_moreInfo_from_db
from Restaurant import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# create_table()

lonasLilEats = Restaurant("Lonas LiL Eats", "/static/images/lonas-lil-eats.jpg", "https://www.google.com/search?q=lonas+lil+eats&rlz=1C5CHFA_enUS855US855&oq=lonas&aqs=chrome.0.69i59j69i57j69i59j0l2j69i60l3.1335j0j7&sourceid=chrome&ie=UTF-8") 
vpSqaure = Restaurant("VP Square", "/static/images/vp-sqaure.jpg", "https://www.google.com/search?q=vp+square&rlz=1C5CHFA_enUS855US855&oq=vp+square&aqs=chrome..69i57j0l5j69i60l2.2166j0j9&sourceid=chrome&ie=UTF-8")
copperPig = Restaurant("Copper Pig", "/static/images/copper-pig.jpg", "https://www.google.com/search?rlz=1C5CHFA_enUS855US855&sxsrf=ALeKk00mDPkZaJA3TRyBIQRvE4E34wwPzg%3A1582071238196&ei=xn1MXpjAC4GztAaUxYXYDA&q=copper+pig&oq=copper+pig&gs_l=psy-ab.3..35i39l3j0l7.498.1067..1575...0.2..0.79.297.4......0....1..gws-wiz.......0i71j0i22i30j0i22i10i30j38j0i20i263.6YitLadtfJU&ved=0ahUKEwiYu6XRqtznAhWBGc0KHZRiAcsQ4dUDCAs&uact=5")
mochiCafe = Restaurant("Mochi Cafe", "/static/images/mochi-cafe.jpg", "https://www.google.com/search?rlz=1C5CHFA_enUS855US855&sxsrf=ACYBGNT1o3smbc6gl43gu1F2_hNFgOTRPA%3A1582071240870&ei=yH1MXpTgNNOQtAbnjaPoAw&q=mochi+cafe&oq=mochi+cafe&gs_l=psy-ab.3..35i39j0l6j0i22i30l3.11857.12792..13021...0.4..0.97.735.10......0....1..gws-wiz.......0i71j0i67j0i273j0i10j0i131.mjj5-YTp3VM&ved=0ahUKEwiU5MjSqtznAhVTCM0KHefGCD0Q4dUDCAs&uact=5")
# southwestMarket = Restaurant("Southwest Market", "southwest-market.jpg", "https://www.google.com/search?q=southwest+market&rlz=1C5CHFA_enUS855US855&oq=south&aqs=chrome.0.69i59j69i57j35i39j0l2j69i60l3.986j0j7&sourceid=chrome&ie=UTF-8")

# data_entry(lonasLilEats)
# data_entry(vpSqaure)
# data_entry(copperPig)
# data_entry(mochiCafe)

restaurantChoices = [lonasLilEats, vpSqaure, copperPig, mochiCafe]

def randomRestaurantSelection():
    value = random.randint(0, len(restaurantChoices)-1)
    return restaurantChoices[value]

name = randomRestaurantSelection().name
image = pull_img_from_db(name)[0]
moreInfo = pull_moreInfo_from_db(name)[0]

@app.route('/result')
def result():
    return render_template('result.html', name=name, image=image, moreInfo=moreInfo)
