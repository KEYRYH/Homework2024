from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello():
    return 'Hello, World'


@app.route('/key')
def key():
    return 'Hello, key123'


if __name__ =="__main__":
    app.run()