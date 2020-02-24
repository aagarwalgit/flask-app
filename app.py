# app.py
from flask import Flask           # import flask
app = Flask(__name__)             # create an app instance

@app.route("/<name>")                   # at the end point /
def hello(name):                      # call method hello
    return "Hello "+name.upper()        # which returns "hello world"
if __name__ == "__main__":        # on running python app.py
    app.run(host='0.0.0.0',port='8080')                     # run the flask app