from flask import Flask, render_template
from db import get_connection, init_db

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/about', methods=['GET'])
def about():
    return render_template('about.html')

@app.route('/services', methods=['GET'])
def services():
    return render_template('services.html')

@app.route('/technology', methods=['GET'])
def technology():
    return render_template('technology.html')

@app.route('/contactform', methods=['GET'])
def contactform():
    return render_template('contactform.html')

if __name__ == '__main__':
    app.run(debug=True)
