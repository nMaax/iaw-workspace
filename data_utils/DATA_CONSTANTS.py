DB_PATH = './static/data/data.db'
ERR_MSG = "Errore nell'accesso al database"

LOREM = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Voluptatum architecto ratione vero? Non quas quisquam tenetur repellendus nam, numquam velit accusantium voluptate animi? Blanditiis voluptas consectetur, nostrum quidem mollitia velit. "

ADMINS = [
    {'username':'akai', 'name': 'Ritsuko', 'surname': 'Akagi', 'description': LOREM*6, 'motto': 'Nessuno conosce il segreto degli eva...', 'monthsago_update': 3, 'propic':'Ritsuko_Akagi.jpeg'},
    {'username':'penpen', 'name': 'Misato', 'surname': 'Katsuragi', 'description': LOREM*6, 'motto': 'Cosa mi nasconde la NERV?', 'monthsago_update': 11, 'propic':'Misato_Katsuragi.jpeg'},
    {'username':'soryuka', 'name': 'Asuka',  'surname':'Soryu Langley', 'description': LOREM*6, 'motto': 'Sono nata per pilotare gli eva', 'monthsago_update': 2, 'propic':'Asuka_Soryu.jpeg'}
]

NON_ADMINS = [
    {'username':'ikarisan', 'name': 'Shinji', 'surname': 'Ikari', 'propic':'Shinji_Ikari.jpeg'},
    {'username':'kaoruni', 'name': 'Kaoru', 'surname': 'Nagisa', 'propic':'Kaoru_Nagisa.jpeg'},
]

POSTS = [
    {'id': 1, 'user': 1, 'date': '2022-12-10', 'text': LOREM*2, 'img':'post1.jpg'},
    {'id': 2, 'user': 2, 'date': '2022-12-10', 'text': LOREM, 'img':'post2.jpg'},
    {'id': 3, 'user': 3, 'date': '2022-12-10', 'text': LOREM, 'img':'post3.jpg'},
]

COMMENTS = [
    {'text':LOREM, 'date': '2022-12-11', 'user': 1, 'post': 1},
    {'text':LOREM, 'date': '2022-12-10', 'user': 1, 'post': 1},
    {'text':LOREM, 'date': '2022-12-11', 'user': 2, 'post': 1},
    {'text':LOREM, 'date': '2022-12-09', 'user': 1, 'post': 2}
]