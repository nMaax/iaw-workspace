# How to install

## Prerequisites

- [Python3](https://www.python.org/) or above
- [A web browser](https://www.mozilla.org/it/firefox/new/)

### Steps

1. Clone this repo in a folder of yours
2. Open a terminal in that folder, then, in the terminal
   1. Generate a python venv (virtual enviroment)
   2. Install ```Flask```, ```Flask-Session``` and ```Bootstrap-Flask```
   3. Run flask with ```flask run``` (eventually add ```--debug``` for debugging)

Copy the following code to complete the step 2 in one shot :rocket:

> For Mac and Linux machines:

```terminal
python3 -m venv venv 
. venv/bin/activate 
pip install Flask, Flask-Session, Bootstrap-Flask
flask --debug run
```

> For Windows machines:

```terminal
python3 -m venv venv 
. venv/bin/activate 
pip install Flask, Flask-Session, Bootstrap-Flask
flask --debug run
```

***

## General Formatting Guidelines

Use the following guidelines to make a clean code, so everyone else will be able to read it better and quickly

> ***Note***
> In **html and css** files: Pretty much i use only kebab-case, except for some ids where i prefer #cammelCaseNotation
> In **python** files: I use prevalently a snake_notation and hungarian notation (hNotation) when needed

### Documentation of tools used

- [Emmet Documentation](https://docs.emmet.io/)
- [Bootstrap Documentation](https://getbootstrap.com/docs/5.2/getting-started/introduction/)
- [Flask Documentation](https://flask.palletsprojects.com/en/2.2.x/)
- [Jinja Documentation](https://jinja.palletsprojects.com/)

### Format of HTML/Bootstrap files

```html
<always indent>
    <tag class="parent-tag-setup padding border margin child-tag-setup gutter personalClass" id="..." style="..." href/src="..."></tag>
<eventually with some spaces>

<!-- and always remember to comment the various sections and other stuff! -->
<if the innested tag is pretty simple (like p, a, h1, img, ...)> <p></p> <you can eventually skip the indentation>
<you can skip indentation too with "skeleton" tags><like head, body and html>
```

#### The scheme of class attribute in html tags basically follows this order

1. Classes that manage how this tag rapports with *parent* tag (tipically: col, nav-item, ...)
2. Classes that manage the styling of *this* tag (other, padding, border, margin - in this order)
3. Classes that manage how this tag rapports with *child* tags (tipically: row, d-flex, ...)
4. Your *personal* classes

> ***Note***
> For breakpoit use **S2G** (From smaller (brekpoint) to greater (breakpoint))
```class class-sm class-md class-lg class-xl class-xxl``` (When in doubt, always specify the 'obvious' classes like col-12)

### Format of CSS files

```css
/* Indentation is important here too! Plus, order of single elements and their attributes is based on gerarchy since this is a *CASCADE* style sheet */

element {
    parent-display-options: ... ;

    display-type: ... ;
    display-options: ... ;
        columns: ... ;
        rows: ... ;

    width: ... ;
    height: ... ;

    text: ... ;
    font: ... ;
    background: ... ;

    other styling attributes: ... ;

    padding: ... ;
    border: ... ;
    margin: ... ;
        top: ... ;
        bottom: ... ;
        right: ... ;
        left: ... ;
 }
 
 /*Always indicate what the following media query do*/
 @media query {
 
    element {
        ...
    }
 
 }

```

### Format of Python/Flask files

```python

# IMPORTS

# Vanilla Python libraries
import os

# External files
from models import User

# Flask libraries
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap5
from flask_session import Session
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

# CONSTANTS

CONSTANT_1 = 'Hi, mom'
CONSTANT_2 = 'NONE'
ISO_DATE = 'YYYY-MM-DD'
UPLOAD_PATH = 'images/uploads'

# DEFINE FLASK APP

app = Flask(__name__)

# CONFING APP

app.secret_key = '?c-xoV-Vkn2&E$q@-tQbX5kCZvve^5'
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

# MAIN ROUTES

@app.route('/')
def index():
   pass
   
...

# Always comment no-html routes, used only for elaboratig data
@app.route('/post_signup', methods=['POST'])
def post_signup():
   pass
   
...

# OTHER ROUTES

@app.route('/test')
def test():
   pass

# OTHER FUNCTIONS

def daysago(sDate):
    if sDate != None and sDate != "":
        dDate = datetime.strptime(sDate, iso_day_format)
        daysago = (datetime.today() - dDate).days
    else:
        daysago = 0

    return daysago

```

### Format of Jinja statements in HTML Files

```html
<!-- Always start with an extend, if needed -->
{% extends 'base.html' %} 

<!-- You can both have multi-line blocks or define them in one line, as you prefer -->
{% block content %}
   
   <!-- Aways indent (except for really short statements), if you dont do it flask will correct it anyway -->
   <div>Hello, world!</div>

   <button>
      {% if current_user.username %}
         {{ current_user.username }}
      {% else %}
         Accedi
      {% endif %}
   </button>

   <!-- Always put some spaces in the inner part of the brakets -->
   <a href="{{ url_for('index') }}" >Look at this link!</a>
   
{% endblock %}

```

## Format of JavaScripts programs

```javascript


```

### How to organize files and folders

- Put html files in the *templates* folder
  - The base html file should be called ```base.html``` or ```layout.html```
- Use the *static* folder only for content that **is not server-generated** but will eventually need to be sent to the client
  - This means that this folder will only manage:
    1. Files that are loaded by the html pages (such as images, videos, gifs etc.)
    2. CSS Stylesheets / Sass files
    3. JavaScript scripts
  - Put images in *static/images*
    - Define a specific sub-folder for every category of file: propics, uploads, ...
  - Put stylesheets in *static/styles*
    - Define a specific sub-folder for every category of file: bootstrap's sheets, personal sheets, extra sheets ...
  - Put sass files in *static/sass*
    - Define a specific sub-folder for every category of file: ...
  - Put scripts in *static/scripts*
    - Define a specific sub-folder for every category of script: ...
- Use the *data* folder for database storage and call the main database as ```data.db```
  - Name the main program to access data.db as ```dao.py``` (Data Access Object)
  - Inside data declare a sub-folder named 'utils'  which will contains all the utils files used by dao.py and other various stuff
- For other extra programs and stuff you don't know where to put use the *misc* (miscellaneous) folder and, eventually, various specific sub-folder, every of them called as sub-folder-name_misc

[![immagine.png](https://i.postimg.cc/wv86ScvP/immagine.png)](https://postimg.cc/DW6kGG1d)

### Useful tips

- Always prefer (if possible) a ```d-flex``` option (```justify, alig-item,``` ...) instead of a "manual" ```padding/margin``` style
- Use *Emmet* and *Flask Snippets* in *VS-Code*!
- If posible use the ```col-auto``` class to make one of the columns in certain row automatically responsive to the changes during breakpoint-switches
