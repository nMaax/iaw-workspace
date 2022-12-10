from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap5
from flask_session import Session

# Various lenght lorem texts
lorem3 = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea, molestiae. Impedit rerum vero aperiam qui accusamus? Culpa deserunt veniam voluptatum aliquam, pariatur perferendis quae aperiam, repellat provident quasi vitae maiores? Eius suscipit repellat repudiandae modi sapiente quam eum facilis? Amet, iste quo. Aliquid adipisci optio accusantium voluptates recusandae consequatur ab placeat deserunt voluptatum soluta in hic voluptatem consequuntur, dolores molestiae. Reprehenderit accusamus numquam voluptatibus maiores doloribus, laudantium saepe. Beatae fuga quisquam deserunt vitae odit dolorem nihil facilis ratione velit rerum eaque sit fugit mollitia eos quas maxime magni, esse accusantium!' 
lorem6 = lorem3*2

admins = [
    {'username':'akai', 'name': 'Ritsuko', 'surname': 'Akagi', 'description': lorem6, 'motto': 'Nessuno conosce il segreto degli eva...', 'monthsago_update': 3, 'propic':'Ritsuko_Akagi.jpeg'},
    {'username':'penpen', 'name': 'Misato', 'surname': 'Katsuragi', 'description': lorem3, 'motto': 'Cosa mi nasconde la NERV?', 'monthsago_update': 11, 'propic':'Misato_Katsuragi.jpeg'},
    {'username':'soryuka', 'name': 'Asuka',  'surname':'Soryu Langley', 'description': lorem6, 'motto': 'Sono nata per pilotare gli eva', 'monthsago_update': 2, 'propic':'Asuka_Soryu.jpeg'}
]

users = [
    {'username':'ikarisan', 'name': 'Shinji', 'surname': 'Ikari', 'propic':'Shinji_Ikari.jpeg'},
    {'username':'kaoruni', 'name': 'Kaoru', 'surname': 'Nagisa', 'propic':'Kaoru_Nagisa.jpeg'},
]

users = users + admins

articles = [
        {'id': 1, 'user': users[0], 'daysago': 2, 'text': lorem6, 'img':'post1.jpg'},
        {'id': 2, 'user': users[1], 'daysago': 3, 'text': lorem3, 'img':'post2.jpg'},
        {'id': 3, 'user': users[3], 'daysago': 5, 'text': lorem3, 'img':'post3.jpg'},
    ]
    
# Defining app
app = Flask(__name__)
app.secret_key="a@owji£je7329fé*oq2c9"
bootstrap = Bootstrap5(app)

# MAIN ROUTES

@app.route('/')
def index():
    #if not session.get('logged_username'):
    #    session['logged_username'] = 'Accedi'
    return render_template('index.html', articles=articles, users=users)

@app.route('/about')
def about():
    return render_template('about.html', admins=admins, users=users)

@app.route('/post/<int:id>')
def post(id):
    index = id-1
    return render_template('post.html', article=articles[index], users=users)

@app.route('/contacts')
def contacts():
    return render_template('contacts.html', users=users)

@app.route('/login', methods = ['POST'])
def login():
    #if request.method == "POST" :
    admin_data = request.form.to_dict()
    session['logged_username'] = admin_data.get('logged_username') 
    return redirect(url_for('index'))

# OTHER ROUTES

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