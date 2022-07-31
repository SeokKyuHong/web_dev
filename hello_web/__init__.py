from flask import Flask, Response, g, make_response

app = Flask(__name__)
app.debug = True

@app.route('/res1')
def res1():
    custom_res = Response("Custom Trsponse", 200, {ttt})
    return make_response(custom_res)

# @app.before_request
# def before_request():
#     print("before_request!!!")
#     g.str = '한글'

@app.route("/gg")
def helloworld_gg():
    return "Hello World!" + getattr(g, 'str', '111')

@app.route("/")
def helloworld():
    return "Hello Flask World!!!!!"