# How to use this repo

A simple project developed during the IAW course at Politecnico di Torino :smiley:

## How to install

## Prerequisites

- [Python3](https://www.python.org/) or above
- A [web browser](https://www.mozilla.org/it/firefox/new/)

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

```

### Format of Jinja statements in HTML Files

```html

```

### Useful tips

- Always prefer (if possible) a ```d-flex``` option (```justify, alig-item,``` ...) instead of a "manual" ```padding/margin``` style
- Use *Emmet* and *Flask Snippets* in *VS-Code*!
- If possible use the ```col-auto``` class to make one of the columns in certain row automatically responsive to the changes during breakpoint-switches
