from flask import Flask, url_for, render_template

lorem3 = 'Lorem ipsum dolor sit amet consectetur adipisicing elit. Ea, molestiae. Impedit rerum vero aperiam qui accusamus? Culpa deserunt veniam voluptatum aliquam, pariatur perferendis quae aperiam, repellat provident quasi vitae maiores? Eius suscipit repellat repudiandae modi sapiente quam eum facilis? Amet, iste quo. Aliquid adipisci optio accusantium voluptates recusandae consequatur ab placeat deserunt voluptatum soluta in hic voluptatem consequuntur, dolores molestiae. Reprehenderit accusamus numquam voluptatibus maiores doloribus, laudantium saepe. Beatae fuga quisquam deserunt vitae odit dolorem nihil facilis ratione velit rerum eaque sit fugit mollitia eos quas maxime magni, esse accusantium!' 
lorem6 = lorem3*2

default_path = ''
propics_path = '/src/propics/'
content_path = '/src/content/'

app = Flask(__name__)

@app.route('/')
def index():

    articles = [
        {'username': 'ikarisan', 'daysago': 2, 'text': lorem6, 'propic':'Shinji_Ikari.jpeg', 'img':'post1.jpg'},
        {'username': 'soryuka', 'daysago': 3, 'text': lorem6, 'propic':'Asuka_Soryu.jpeg', 'img':'post2.jpg'},
        {'username': 'kaoruni', 'daysago': 5, 'text': lorem6, 'propic':'Kaoru_Nagisa.jpeg', 'img':'post3.jpg'},
    ]

    for article in articles :
        article['propic'] = propics_path + article['propic']
        article['img'] = content_path + article['img']
    
    return render_template('index.html', page='home', articles=articles)

@app.route('/about')
def about():

    developers = [
        {'fullname': 'Ritsuko Akagi', 'description': lorem6, 'motto': 'Nessuno conosce il segreto degli eva...', 'monthsago_update': 3, 'propic':''},
        {'fullname': 'Misato Katsuragi', 'description': lorem3, 'motto': 'Cosa mi nasconde la NERV?', 'monthsago_update': 11, 'propic':''},
        {'fullname': 'Asuka Soryu Langley', 'description': lorem6, 'motto': 'Sono nata per pilotare gli eva', 'monthsago_update': 2, 'propic':''}
    ]



    return render_template('about.html', page='about', developers=developers)

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