# Vanilla Python libraries
import os
#import re
from datetime import datetime, date
#import sqlite3

# External files
import data_utils.access_data as db
from models import User

# Flask libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
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
app.secret_key = '?c-xoV-Vkn2&E$q@-tQbX5kCZvve^5'

# Defining app attributes and other setups
UPLOAD_FOLDER = './static/images/uploads/'
PROPIC_FOLDER = './static/images/propics/'
SECRET_KEY = 'Z2KRu#3+5Ps?ngrxT&!icMR?pC$krH'
SESSION_TYPE = 'filesystem'
SESSION_PERMANENT = False

app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['PROPIC_FOLDER'] = PROPIC_FOLDER
app.config['SESSION_TYPE'] = SESSION_TYPE
app.config['SESSION_PERMANENT'] = SESSION_PERMANENT

bootstrap = Bootstrap5(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

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

@app.route('/signup')
def signup():
    return render_template('signup.html')

# TODO list
# [ ] Resolve same image in different post bug

# No-html route, used only for elaboratig data
@app.route('/post_signup', methods=['POST'])
def post_signup():
    username = request.form.get('username')
    name = request.form.get('name')
    surname = request.form.get('surname')
    password = request.form.get('password')

    user_in_db = db.get_user_by_username(username)
    success = False

    if not user_in_db:
        user = {
            'username': username,
            'name': name,
            'surname': surname,
            'password': generate_password_hash(password, method='sha256')
        }
        db.add_user(user, admin = False)
        success = True

    if success:
        propic = request.files.get('propic')
        filename = username+'.jpeg'
        # Save it in the right place with os.path.join()
        propic.save(os.path.join(app.config['PROPIC_FOLDER'], filename))
        print(propic)
        flash('Iscrizione effettuata', 'success')
        app.logger.info('\n\n* * * ISCRIZIONE EFFETTUATA CORRETTAMENTE * * *\n')
        # Automatic login
        post_login()
    else:
        flash('Iscrizione non effettuata, dati inseriti erronei', 'warning')
        app.logger.error('\n\n* * * ISCRIZIONE NON EFFETTUATA * * *\n')

    app.logger.info(' --> Username: ' + username)
    return redirect(url_for('index'))

# No-html route, used only for elaboratig data
@app.route('/post_login', methods=['POST'])
def post_login():
    username = request.form.get('username') 
    password = request.form.get('password')

    user = db.get_user_by_username(username)

    if user and check_password_hash(user.get('password'), password):
        logged_user = User(id=user.get('id'), username=user.get('username'), password=user.get('password'),name=user.get('name'), surname=user.get('surname'))
        login_user(logged_user, True)
        flash('Login effettuato', 'success')
        app.logger.info('\n\n* * * LOGIN EFFETTUATO CORRETTAMENTE * * *\n')
    else:
        flash('Login non effettuato, dati inseriti erronei', 'danger')
        app.logger.error('\n\n* * * LOGIN NON EFFETTUATO * * *\n')

    app.logger.info(' --> Username: ' + str(username) )

    return redirect(url_for('index'))

@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash('Logout effettuato', 'info')
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

@app.route('/post/<int:post_id>/new_comment_<username>', methods=['POST'])
def new_comment(post_id, username):
    
    comment_to_add = {}
    
    comment_to_add['text'] = request.form.get('text')
    comment_to_add['post_id'] = post_id
    comment_to_add['username'] = username

    for user in db.get_users():
        if user.get('username') == username:
            comment_to_add['user_id'] = user.get('id')
    comment_to_add['date'] = utils.get('today')

    db.add_comment(comment_to_add)

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
    #id = posts[-1].get('id')+1
    id = db.get_last_post().get('id')+1
    post = {'id': id, 'user_id': -1, 'date': -1, 'text': 'NO_TEXT', 'img': 'NO_IMG'}
    abort = False

    app.logger.info(id)
    for post in posts:
        app.logger.info(post)

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
        app.logger.info(filename)
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
    else:
        flash('Dati inseriti erronei, post non creato', 'danger')
        app.logger.error('* * * POST NON CREATO * * *')

    return redirect(url_for('index'))  

# Other functions
@login_manager.user_loader
def load_user(user_id):
    db_user = db.get_user_by_id(user_id)

    user = User(id=db_user['id'], username=db_user['username'], password=db_user['password'], name=db_user['name'], surname=db_user['surname'])

    return user 

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