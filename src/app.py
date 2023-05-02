#!/bin/python
from flask import Flask
from endpoints import counttokensAPI

def create_app():
    app = Flask(__name__)
    
    app.register_blueprint(counttokensAPI)
    
    return app

if __name__ == '__main__':
    # run app in debug mode on port 5000
    app = create_app()
    app.run(debug=True, port=5000)