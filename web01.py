from flask import json
from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def api_root():
    return "Hola"

if __name__ == '__main__':
    app.run(debug=True)