import os
import socket
import random
from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates')

color_codes = {
    "red": "#e74c3c",
    "green": "#16a085",
    "blue": "#2980b9",
    "blue2": "#30336b",
    "pink": "#be2edd",
    "darkblue": "#130f40"
}

color = os.environ.get('APP_COLOR') or random.choice(
    ["red", "green", "blue", "blue2", "pink", "darkblue"])


@app.route('/')
def main():
    # return "Welcome! Update 2"
    print(color)
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[color])


@app.route('/color/<new_color>')
def new_color(new_color):
    return render_template('hello.html', name=socket.gethostname(), color=color_codes[new_color])


@app.route('/how are you')
def hello():
    return "I am good, how about you?"


@app.route('/read_file')
def read_file():
    f = open("/data/testfile.txt")
    contents = f.read()
    return render_template('hello.html', name=socket.gethostname(), contents=contents, color=color_codes[color])


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
