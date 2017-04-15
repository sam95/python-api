from flask import Flask
from resources.TrySearch import search_api

DEBUG = True

app = Flask(__name__)
app.register_blueprint(search_api)


@app.route('/')
def hello_world():
    return 'Hello world'


if __name__ == '__main__':
    app.run(debug=DEBUG, host = '0.0.0.0')
