from crypt import methods
from re import template
from flask import Flask, request

import hello_web

app = Flask(__name__)

@app.route(hello_web/templates/index.html)

@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login('/')
    else :
        return show_the_login_from('hello_web/templates/index.html'))

app.run(port=5003, debug=True)