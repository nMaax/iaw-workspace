from flask import Flask, url_for, render_template

app = Flask(__name__)

@app.route('/')
def index():
    articles = [
        {'username': 'ikarisan', 'daysago': 2, 'text': '🦉'},
        {'username': 'soryuka', 'daysago': 3, 'text': 'Sono nata per pilotare gli eva!'},
        {'username': 'kaoruni', 'daysago': 5, 'text': ':('},
    ]
    return render_template('index.html', page='home', articles=articles)

@app.route('/about')
def about():
    return render_template('about.html', page='about')

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