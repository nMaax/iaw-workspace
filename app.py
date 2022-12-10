from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_bootstrap import Bootstrap5
from flask_session import Session

# Various lenght lorem texts
lorem3 = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea, molestiae. Impedit rerum vero aperiam qui accusamus? Culpa deserunt veniam voluptatum aliquam, pariatur perferendis quae aperiam, repellat provident quasi vitae maiores? Eius suscipit repellat repudiandae modi sapiente quam eum facilis? Amet, iste quo. Aliquid adipisci optio accusantium voluptates recusandae consequatur ab placeat deserunt voluptatum soluta in hic voluptatem consequuntur, dolores molestiae. Reprehenderit accusamus numquam voluptatibus maiores doloribus, laudantium saepe. Beatae fuga quisquam deserunt vitae odit dolorem nihil facilis ratione velit rerum eaque sit fugit mollitia eos quas maxime magni, esse accusantium!' 
lorem6 = lorem3*2

articles = [
        {'id': 1, 'username': 'ikarisan', 'daysago': 2, 'text': lorem6, 'propic':'Shinji_Ikari.jpeg', 'img':'post1.jpg'},
        {'id': 2, 'username': 'soryuka', 'daysago': 3, 'text': lorem3, 'propic':'Asuka_Soryu.jpeg', 'img':'post2.jpg'},
        {'id': 3, 'username': 'kaoruni', 'daysago': 5, 'text': lorem3, 'propic':'Kaoru_Nagisa.jpeg', 'img':'post3.jpg'},
    ]

developers = [
    {'fullname': 'Ritsuko Akagi', 'description': lorem6, 'motto': 'Nessuno conosce il segreto degli eva...', 'monthsago_update': 3, 'propic':'Ritsuko_Akagi.jpeg'},
    {'fullname': 'Misato Katsuragi', 'description': lorem3, 'motto': 'Cosa mi nasconde la NERV?', 'monthsago_update': 11, 'propic':'Misato_Katsuragi.jpeg'},
    {'fullname': 'Asuka Soryu Langley', 'description': lorem6, 'motto': 'Sono nata per pilotare gli eva', 'monthsago_update': 2, 'propic':'Asuka_Soryu.jpeg'}
]
    
# Defining app
app = Flask(__name__)
app.secret_key="a@owji£je7329fé*oq2c9"
bootstrap = Bootstrap5(app)

# MAIN ROUTES

@app.route('/')
def index():
    if not session.get('admin_name'):
        session['admin_name'] = 'Accedi'
    return render_template('index.html', articles=articles)

@app.route('/about')
def about():
    return render_template('about.html', developers=developers)

@app.route('/post/<int:id>')
def post(id):
    return render_template('post.html', article=articles[id-1])

@app.route('/admin_access', methods = ['POST'])
def admin_access():
    admin_data = request.form.to_dict()
    session['admin'] = True
    session['admin_name'] = admin_data.get('admin_name') 
    return redirect(url_for('index'))

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

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