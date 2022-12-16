from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import delete, update, Boolean, select
from sqlalchemy import text

"""
----- CREATE TABLE IN DATABASE IN TERMINAL-----
flask shell
from app import db
db.create_all()
"""

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@127.0.0.1/point_of_sale_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Clerk(db.Model):
    __tablename__ = 'clerk'
    
    id_clerk = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255))

    # Create relationship
    transactions = db.relationship('Invoice', backref='invoice')

    def __init__(self, id_clerk, username, password):
        self.id_clerk = id_clerk
        self.username = username
        self.password = password

class Product(db.Model):
    __tablename__ = 'product'
    
    id_product = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(255))
    price = db.Column(db.Integer)
    category = db.Column(db.String(255))
    
    def __init__(self, id_product, product_name, price, category):
        self.id_product = id_product
        self.product_name = product_name
        self.price = price
        self.category = category

class Invoice(db.Model):
    __tablename__ = 'invoice'
    
    id_invoice = db.Column('id_invoice', db.Integer, primary_key=True)
    id_clerk = db.Column(db.Integer, db.ForeignKey('clerk.id_clerk'))
    date = db.Column(db.Date)
    
    def __init__(self, id_clerk, date):
        self.id_clerk = id_clerk
        self.date = date

# class InvoiceDetail(db.Model):
#     __tablename__ = 'invoice_detail'
    
#     id_invoice = db.Column(db.Integer, db.ForeignKey('invoice.id_invoice'))
#     id_product = db.Column(db.Integer, db.ForeignKey('product.id_product'))
#     quantity = db.Column(db.Integer)
#     total = db.Column(db.Integer)
    
#     def __init__(self, id_invoice, id_product, quantity, total):
#         self.id_invoice = id_invoice
#         self.id_product = id_product
#         self.quantity = quantity
#         self.total = total

"""
INSERT INTO `clerk` (`username`, `password`) VALUES 
("Victor", 12345678),
("Jacob", 87654321),
("Filbert", qwerasdf)

INSERT INTO `product` (`product_name`, `price`, `category`) VALUES 
("Pisang Goreng", 15000, "Goreng"),
("Nasi Goreng", 20000, "Goreng"),
("Ayam Goreng", 17000, "Goreng"),
("Sop Ayam", 18000, "Soup"),
("Soto Ayam", 17000, "Soup"),
("Bakso", 14000, "Soup"),
("Coca-cola", 10000, "Minuman"),
("Es Teh Manus", 8000, "Minuman"),
("Es Jeruk", 12000, "Minuman")
"""
