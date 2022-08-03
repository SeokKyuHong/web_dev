from crypt import methods
from turtle import title
from flask import Flask, render_template, request, redirect
from pyngrok import conf, ngrok

app = Flask(__name__)

nextId = 4
topics = [
    {'id': 1, 'title': 'html', 'body': 'html is ...'},
    {'id': 2, 'title': 'css', 'body': 'css is ...'},
    {'id': 3, 'title': 'javascript', 'body': 'javascript is ...'}
]

@app.route("/")
def hello_world():
    return render_template('index.html')

# @app.route("{Directory}")
# def {function name}():
#     return {Return data}

@app.route("/finder")
def new_link():
    return render_template('finder.html')

@app.route("/create/", methods=['GET','POST'])
def new_create():
    if request.method == 'GET':
        return render_template('create.html')
    elif request.method == 'POST':
        global nextId
        title = request.form['title']
        body = request.form['body']
        newTopic = {'id': nextId, 'title': title, 'body': body}
        topics.append(newTopic)
        url = "/read/" + str(nextId)+'/'
        nextId = nextId +1
        return title+','+body


app.run(port=5001, debug=True)