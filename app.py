from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return ""

@app.route('/chi_siamo')
def chi_siamo():
    return ""