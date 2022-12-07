from flask import Flask, url_for, render_template

# Various lenght lorem texts
lorem3 = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea, molestiae. Impedit rerum vero aperiam qui accusamus? Culpa deserunt veniam voluptatum aliquam, pariatur perferendis quae aperiam, repellat provident quasi vitae maiores? Eius suscipit repellat repudiandae modi sapiente quam eum facilis? Amet, iste quo. Aliquid adipisci optio accusantium voluptates recusandae consequatur ab placeat deserunt voluptatum soluta in hic voluptatem consequuntur, dolores molestiae. Reprehenderit accusamus numquam voluptatibus maiores doloribus, laudantium saepe. Beatae fuga quisquam deserunt vitae odit dolorem nihil facilis ratione velit rerum eaque sit fugit mollitia eos quas maxime magni, esse accusantium!' 
lorem6 = lorem3*2

# Defining app
app = Flask(__name__)

# MAIN ROUTES

@app.route('/')
def index():

    articles = [
        {'username': 'ikarisan', 'daysago': 2, 'text': lorem6, 'propic':'Shinji_Ikari.jpeg', 'img':'post1.jpg'},
        {'username': 'soryuka', 'daysago': 3, 'text': lorem6, 'propic':'Asuka_Soryu.jpeg', 'img':'post2.jpg'},
        {'username': 'kaoruni', 'daysago': 5, 'text': lorem6, 'propic':'Kaoru_Nagisa.jpeg', 'img':'post3.jpg'},
    ]
    
    return render_template('index.html', articles=articles)

@app.route('/about')
def about():

    developers = [
        {'fullname': 'Ritsuko Akagi', 'description': lorem6, 'motto': 'Nessuno conosce il segreto degli eva...', 'monthsago_update': 3, 'propic':'Ritsuko_Akagi.jpeg'},
        {'fullname': 'Misato Katsuragi', 'description': lorem3, 'motto': 'Cosa mi nasconde la NERV?', 'monthsago_update': 11, 'propic':'Misato_Katsuragi.jpeg'},
        {'fullname': 'Asuka Soryu Langley', 'description': lorem6, 'motto': 'Sono nata per pilotare gli eva', 'monthsago_update': 2, 'propic':'Asuka_Soryu.jpeg'}
    ]

    return render_template('about.html', developers=developers)

@app.route('/post')
def post():
    return render_template('post.html')

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