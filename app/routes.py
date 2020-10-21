from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username' : 'Sunny Lopez'}
    posts = [
        {
            'author' : {'username' : 'John'},
            'body' : 'Beautiful day in Los Angeles'
        },
        {
            'author' : {'username' : 'Susan'},
            'body' : "Movie was cool"
        }
    ]
    return render_template('index.html', title='Home', user=user, posts = posts)
