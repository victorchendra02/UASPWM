from db import *


@app.route('/users', methods=['GET', 'POST'])
def adf():
    a = [
        {"id": 1,  "name": "food"},
        {"id": 2,  "name": "mouse"},
        {"id": 3,  "name": "drink"},
        ]
    return a

@app.route('/invoice', methods=['POST'])
def aaa():
    a = [
        {"id": 1,  "name": "food"},
        {"id": 2,  "name": "mouse"},
        {"id": 3,  "name": "drink"},
        ]
    return a
