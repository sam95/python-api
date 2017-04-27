from flask import Flask
from resources.MinEng import search_api

DEBUG = True

app = Flask(__name__)
app.register_blueprint(search_api)


if __name__ == '__main__':
    app.run(debug=DEBUG, host = '0.0.0.0')
