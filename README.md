# How to use this repo

Read the following file to understend how to use this

## How to install

## Prerequisites

- Python 3
- A web browser

### Steps

1. Clone this repo in a folder of yours
2. Open a terminal
   1. Generate a python venv (virtual enviroment)
   2. Install ```Flask```, ```Flask-Session``` and ```Bootstrap-Flask```
   3. Run it

Copy the following code to complete the step 2 in one shot

```terminal
python3 -m venv venv 
. venv/bin/activate 
pip install Flask, Flask-Session, Bootstrap-Flask
flask --debug run
```

***

## General Formatting Guidelines

Use the following guidelines to make a clean code, so everyone else will be able to read it better and quickly

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

#### The scheme of classes is basically

1. Manage how this tag rapports with _parent_ tag (tipically: col, nav-item, ...)
2. Manage the styling of _this_ tag (other, padding, border, margin - in this order)
3. Manage how this tag rapports with _child_ tags (tipically: row, d-flex, ...)
4. You _personal classes_
5. For breakpoit use **S2G** (From smaller (brekpoint) to greater (breakpoint))
    - class class-sm class-md class-lg class-xl class-xxl
    - When in doubt, always specify the 'obvious' classes like col-12

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
- Use _Emmet_ and _Flask Snippets_ in _VS-Code_!
- If possible use the ```col-auto``` class to make one of the columns in certain row automatically responsive to the changes during breakpoint-switches
