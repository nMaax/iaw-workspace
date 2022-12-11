# Vanilla Python libraries
import os
import re
from datetime import datetime, date

# Flask libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from flask_bootstrap import Bootstrap5
from flask_session import Session

# Defining today as a string
now = datetime.now()
date_string = now.strftime('%Y-%m-%d')

# Defining an utils dict to be used where needed
utils = {'today': date_string, 'lorem': lorem}
    
# Defining app
app = Flask(__name__)

# Defining app attributes
UPLOAD_FOLDER = './static/images/uploads/'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False

# Generating objects for Flask extra libraries
Session(app)
bootstrap = Bootstrap5(app)

# Main routes

@app.route('/')
def index():
    return render_template('index.html', posts=posts, users=users, utils=utils)

@app.route('/about')
def about():
    return render_template('about.html', admins=admins, users=users, utils=utils)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', users=users, utils=utils)

# No-html route, used only for elaboratig data
@app.route('/login', methods = ['POST'])
def login():
    admin_data = request.form.to_dict()
    session['logged_username'] = admin_data.get('logged_username') 
    flash('Login effettuato', 'success')
    app.logger.debug('\n\n* * * LOGIN EFFETTUATO CORRETTAMENTE * * *\n')
    return redirect(url_for('index'))

@app.route('/post/<int:id>')
def post(id):
    index = id-1
    return render_template('post.html', post=posts[index], users=users, utils=utils)

# No-html route, used only for elaboratig data
@app.route('/post/new', methods=['POST'])
def new_post():
    # Retrive data from the form
    data = request.form.to_dict()
    img = request.files.get('img')
    
    # Default post values
    id = posts[-1].get('id')+1
    post = {'id': id, 'user': None, 'daysago': -1, 'text': 'NO_TEXT', 'img': 'NO_IMG'}
    abort = False

    # Searching for the user in the data structure
    for user in users:
        if user.get('username') == data.get('username'):
            post['user'] = user

    # The date must be in the right format
    sDate = data.get('date')
    if sDate != None and sDate != "":
        dDate = datetime.strptime(sDate, '%Y-%m-%d')
        daysago = (datetime.today() - dDate).days
    else:
        daysago = 0
    # Date must be before or equal today
    if (daysago >= 0):
        post['daysago'] =  daysago
    # Data is mandatory
    else:
        post['daysago'] = 'INVALID_DATE'
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
    
    # Debugging what happened
    if not abort:
        posts.append(post)
        flash('Post creato correttamente', 'success')
        app.logger.debug('Created post with:\n    > id: '+str(post.get('id'))+'\n    > user: '+post.get('user').get('username')+'\n    > text: '+post.get('text')+'\n    > image: '+post.get('img'))
    else:
        flash('Dati inseriti erronei, post non creato', 'danger')
        app.logger.debug('\n\n* * * INVALID FORM, NO POST HAS BEEN CREATED * * *\n')
    
    return redirect(url_for('index'))

# Other routes

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html')

@app.route('/test')
def test():
    
    # Lista di dizionari
    pilots = [  {'name': 'Shinji', 'surname': 'Ikari'},
                {'name': 'Rei', 'surname': 'Ayanami'},
                {'name': 'Asuka', 'surname': 'Langley Soryu'},
                {'name': 'Toji', 'surname': 'Suzuhara'},
                {'name': 'Kaoru', 'surname': 'Nagisa'}
            ]
    
    avaible_pilots = pilots.copy()
    for avaible_pilot in avaible_pilots:
        if (avaible_pilot.get('name') == 'Shinji' or avaible_pilot.get('surname') == 'Ikari'):
            avaible_pilots.remove(avaible_pilot)

    human_pilots=[{'name': 'Shinji', 'surname': 'Ikari'},{'name': 'Asuka', 'surname': 'Langley Soryu'},{'name': 'Toji', 'surname': 'Suzuhara'}]
    return render_template('test.html', pilots = pilots, avaible_pilots=avaible_pilots, human_pilots=human_pilots)