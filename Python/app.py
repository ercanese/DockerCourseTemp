from flask import Flask
import os

app = Flask(__name__)

@app.route('/')

def hello_world():
    return '<h2>Hello World</h2>'


if __name__ == '__main__':
    app.run()