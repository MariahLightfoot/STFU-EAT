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

# create_table()

# lonas = Restaurant("Lonas LiL Eats", "/static/images/lonas-lil-eats.jpg") 
# vpSqaure = Restaurant("VP Square", "vp-sqaure.jpg")
# copperPig = Restaurant("Copper Pig", "copper-pig.jpg")
# mochiCafe = Restaurant("Mochi Cafe", "mochi-cafe.jpg")
# southwestMarket = Restaurant("Southwest Market", "southwest-market.jpg")

# data_entry(lonas)

