# Vanilla Python libraries
import os
import re
from datetime import datetime, date
import sqlite3

# External files
import data_utils.access_data as db

# Flask libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap5
from flask_session import Session

# Defining today as a string
now = datetime.now()
date_string = now.strftime('%Y-%m-%d')

# Defining an utils dict to be used where needed
utils = {'today': date_string}
    
# Defining app
app = Flask(__name__)

# Defining app attributes
UPLOAD_FOLDER = './static/images/uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False

# Generating objects for Flask extra libraries
# TODO basta questo per avere sessioni server side?
Session(app)
bootstrap = Bootstrap5(app)

# Main routes

@app.route('/')
def index():
    users = db.get_users()
    posts = db.get_posts()
    add_user_to_posts(posts=posts, users=users)
    add_daysago_to_posts(posts=posts)
    return render_template('index.html', posts=posts, users=users, utils=utils)

@app.route('/about')
def about():
    users=db.get_users()
    admins=db.get_admins()
    return render_template('about.html', admins=admins, users=users, utils=utils)

@app.route('/contacts')
def contacts():
    users=db.get_users()
    return render_template('contacts.html', users=users, utils=utils)

# No-html route, used only for elaboratig data
@app.route('/login', methods = ['POST'])
def login():
    admin_data = request.form.to_dict()

    usernames = []
    users=db.get_users()
    for user in users:
        usernames.append(user.get('username'))

    if admin_data['logged_username'] in usernames:
        session['logged_username'] = admin_data.get('logged_username')
        flash('Login effettuato', 'success')
        app.logger.info('\n\n* * * LOGIN EFFETTUATO CORRETTAMENTE * * *\n')
        app.logger.info(' --> Username: ' + str(admin_data['logged_username']) )
    else:
        flash('Login non effetto, dati inseriti erronei', 'danger')
        app.logger.error('\n\n* * * LOGIN NON EFFETTUATO * * *\n')

    return redirect(url_for('index'))

@app.route('/post/<int:id>')
def post(id):
    index = id-1
    users=db.get_users()
    posts=db.get_posts()
    add_user_to_posts(posts=posts, users=users)
    return render_template('post.html', post=posts[index], users=users, utils=utils)

# No-html route, used only for elaboratig data
@app.route('/post/new', methods=['POST'])
def new_post():
    users=db.get_users()
    posts=db.get_posts()
    add_user_to_posts(posts=posts, users=users)

    # Retrive data from the form
    data = request.form.to_dict()
    img = request.files.get('img')
    
    # Default post values
    id = posts[-1].get('id')+1
    post = {'id': id, 'user_id': -1, 'date': -1, 'text': 'NO_TEXT', 'img': 'NO_IMG'}
    abort = False

    # Searching for the user in the data structure
    trovato = False
    for user in users:
        if user.get('username') == data.get('username'):
            post['user_id'] = user.get('id')
            trovato = True
    if not trovato: 
        abort = True
    
    # The date must be in the right format
    sDate = data.get('date')
    daysago_ = daysago(sDate)
    # Date must be before or equal today
    if (daysago_ >= 0):
        post['date'] =  sDate
    # Data is mandatory
    else:
        post['date'] = 'INVALID_DATE'
        abort = True

    # The text must be in the right format
    text = data.get('text')
    post_lenght = len(text)
    # Minimum 30 and maximum 200 character
    if (post_lenght >= 1 and post_lenght <= 1000):
        post['text'] = text
    # Text is mandatory
    else:
        post['text'] = 'INVALID_TEXT'
        abort = True

    # Image is not mandatory
    if img:
        # Rename the image in order to don't have problems
        filename = 'post'+str(id)+'.jpg'
        # Save it in the right place with os.path.join()
        img.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
    else:
        # Default image in case it is not defined
        filename = 'logo.png'
    # Add it to the data structure    
    post['img'] = filename
    
    # Notificate if the where any errors
    if not abort:
        db.add_post(post)
        flash('Post creato correttamente', 'success')
        app.logger.info('* * * POST CREATO CORRETTAMENTE * * *')
        app.logger.info(' --> post_id:'+str(post['id'])+', user_id:'+str(post['user_id']))
    else:
        flash('Dati inseriti erronei, post non creato', 'danger')
        app.logger.error('* * * POST NON CREATO * * *')

    return redirect(url_for('index'))

# Utils functions

def add_user_to_posts(posts, users):
    for post in posts:
        for user in users:
            if user['id'] == post['user_id']:
                connected_user = user
        post['user'] = connected_user

def add_daysago_to_posts(posts):
    for post in posts:
        post['daysago'] = daysago(post.get('date'))

def daysago(sDate):
    if sDate != None and sDate != "":
        dDate = datetime.strptime(sDate, '%Y-%m-%d')
        daysago = (datetime.today() - dDate).days
    else:
        daysago = 0

    return daysago