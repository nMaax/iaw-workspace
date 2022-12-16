# Vanilla Python libraries
import os
#import re
from datetime import datetime, date
#import sqlite3

# External files
import data_utils.access_data as db

# Flask libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap5
from flask_session import Session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

# Defining an utils dict to be used whenever is needed

iso_day_format  = '%Y-%m-%d'

#Today day value
now = datetime.now()
sNow = now.strftime(iso_day_format)

utils = {'today': sNow}
    
# Defining app
app = Flask(__name__)

# Generating objects for Flask extra libraries (Server-side sessions and Bootstrap)
bootstrap = Bootstrap5(app)

# Defining app attributes
UPLOAD_FOLDER = './static/images/uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False

Session(app)

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
    users=db.get_users()
    posts=db.get_posts()
    add_user_to_posts(posts=posts, users=users)
    for post_ in posts:
        if post_['id'] == id:
            post = post_
    add_comments_to_post(post)
    return render_template('post.html', post=post, users=users, utils=utils)

@app.route('/post/<int:post_id>/new_comment/<username>', methods=['POST'])
def add_comment(post_id, username):
    new_comment = request.form.to_dict()
    new_comment['post_id'] = post_id
    new_comment['username'] = username
    for user in db.get_users():
        if user.get('username') == username:
            new_comment['user_id'] = user.get('id')
    new_comment['date'] = utils.get('today')
    db.add_comment(new_comment)
    return redirect(url_for('post', id=post_id))

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

# Other functions

# Functions to add new data to post dict
def add_user_to_posts(posts, users):
    for post in posts:
        for user in users:
            if user['id'] == post['user_id']:
                connected_user = user
        post['user'] = connected_user

def add_daysago_to_posts(posts):
    for post in posts:
        post['daysago'] = daysago(post.get('date'))

def add_comments_to_post(post):
    post_id = post.get('id')
    comments = db.get_comments(post_id)
    for comment in comments:
        add_user_to_comment(comment)
        add_daysago_to_comment(comment)
    post['comments'] = comments

def add_user_to_comment(comment):
    commenter_id = comment.get('user_id')
    commenter = db.get_user(commenter_id)
    comment['user'] = commenter

def add_daysago_to_comment(comment):
    daysago_ = daysago(comment.get('date'))
    comment['daysago'] = daysago_

# Function that returns how many days are passed since the date passed as parameter as "YYYY-MM-DD"
def daysago(sDate):
    if sDate != None and sDate != "":
        dDate = datetime.strptime(sDate, iso_day_format)
        daysago = (datetime.today() - dDate).days
    else:
        daysago = 0

    return daysago