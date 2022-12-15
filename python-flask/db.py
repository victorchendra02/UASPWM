from flask import Flask, render_template, request, redirect
# from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete, update, Boolean, select
from sqlalchemy import text

"""
----- CREATE TABLE IN DATABASE IN TERMINAL-----
flask shell
from app import db
db.create_all()
"""

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/debt_database'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


@app.route('/category', methods=['GET', 'POST'])
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



app.run()
