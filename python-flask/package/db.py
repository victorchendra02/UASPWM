from flask import Flask, render_template, request, redirect, jsonify, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete, update, Boolean, select
from sqlalchemy import text
from flask_cors import CORS
from datetime import date
import os

"""
1. Create table
activate the environment first
----- CREATE TABLE IN DATABASE IN TERMINAL -----
flask shell
from app import db
db.create_all()
"""

"""
2. Insert default data
INSERT INTO `clerk` (`username`, `password`) VALUES 
("Victor", "12345678"),
("Jacob", "87654321"),
("Filbert", "qwerasdf");

INSERT INTO `product` (`product_name`, `price`, `category`, `img_path`) VALUES 
("Pisang Goreng", 15000, "Goreng", "http://127.0.0.1:5000/static/images/gorengan/pisanggoreng.jpg"),
("Nasi Goreng", 20000, "Goreng", "http://127.0.0.1:5000/static/images/gorengan/nasigoreng.jpg"),
("Ayam Goreng", 17000, "Goreng", "http://127.0.0.1:5000/static/images/gorengan/ayamgoreng.jpg"),
("Sop Ayam", 18000, "Soup", "http://127.0.0.1:5000/static/images/gorengan/sopayam.jpg"),
("Soto Ayam", 17000, "Soup", "http://127.0.0.1:5000/static/images/gorengan/sotoayam.jpg"),
("Bakso", 14000, "Soup", "http://127.0.0.1:5000/static/images/gorengan/bakso.jpg"),
("Coca-cola", 10000, "Minuman", "http://127.0.0.1:5000/static/images/gorengan/cocacola.jpg"),
("Es Teh Manis", 8000, "Minuman", "http://127.0.0.1:5000/static/images/gorengan/estehmanis.jpg"),
("Es Jeruk", 12000, "Minuman", "http://127.0.0.1:5000/static/images/gorengan/esjeruk.jpg");

"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/point_of_sale_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Create path to display images where our images stored in database (img_path)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
app.config['UPLOADED_PHOTOS_DEST'] = os.path.join(APP_ROOT, 'images')

# This is to give our "front end access" to our API
CORS(app, resources={r"*": {"origins": "*"}})

class Clerk(db.Model):
    __tablename__ = 'clerk'
    
    id_clerk = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    # Create relationship
    transactions = db.relationship('Invoice', backref='invoice')

    def __init__(self, username, password):
        self.username = username
        self.password = password

class Product(db.Model):
    __tablename__ = 'product'
    
    id_product = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    category = db.Column(db.String(255))
    img_path = db.Column(db.Text)
    
    # Create relationship
    transactions = db.relationship('InvoiceDetail', backref='invoice_detail')
    
    def __init__(self, product_name, price, category):
        self.product_name = product_name
        self.price = price
        self.category = category

class Invoice(db.Model):
    __tablename__ = 'invoice'
    
    id_invoice = db.Column('id_invoice', db.Integer, primary_key=True, autoincrement=True)
    id_clerk = db.Column(db.Integer, db.ForeignKey('clerk.id_clerk'))
    date = db.Column(db.Date)
    
    # Create relationship
    invoice_detail = db.relationship('InvoiceDetail', backref='invoice')
    
    def __init__(self, id_clerk, date):
        self.id_clerk = id_clerk
        self.date = date

class InvoiceDetail(db.Model):
    __tablename__ = 'invoice_detail'
    
    id_idetail = db.Column('id_idetail', db.Integer, primary_key=True, autoincrement=True)
    id_invoice = db.Column(db.Integer, db.ForeignKey('invoice.id_invoice'))
    id_product = db.Column(db.Integer, db.ForeignKey('product.id_product'))
    quantity = db.Column(db.Integer)
    sub_total = db.Column(db.Integer)
    
    def __init__(self, id_invoice, id_product, quantity, sub_total):
        self.id_invoice = id_invoice
        self.id_product = id_product
        self.quantity = quantity
        self.sub_total = sub_total
