import sqlite3, config
from flask import Flask, render_template, request

app = Flask(__name__)

def connect_db():
    return sqlite3.connect(config.STFU-EAT.db)

@app.route('/')
def index():
    db_connection = connect_db()
    cursor = db_connection.execute('SELECT id, name, image FROM local-stl-restaurants;')
    return render_template('index.html')

@app.route('/result', methods=['GET', 'POST'])
def result():
    if request.method == 'GET':
        return render_template('result.html')

if __name__ == '__main__':
    app.run(debug=True)