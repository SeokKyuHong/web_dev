from flask import Flask, render_template
from pyngrok import conf, ngrok

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

# @app.route("{Directory}")
# def {function name}():
#     return {Return data}

@app.route("/finder")
def new_link():
    return render_template('finder.html')


# app.run(debug=True)
if __name__ == '__main__':
    app.debug = True
    app.run()