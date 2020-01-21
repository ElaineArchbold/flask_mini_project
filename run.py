import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello there!</>"

app.run(host=os.getenv('IP'), port=int(os.getenv('PORT')), debug=True)