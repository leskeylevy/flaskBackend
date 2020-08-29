import datetime
import uuid

from app.main import db
from app.main.model.products import Products


def save_new_product(data):
    new_product = Products(
        name=data['name'],
        description=data['description'],
        created_on=datetime.datetime.utcnow(),
        status='New',
        producId=str(uuid.uuid4()),
        supplierId=data['supplierId'],
        category=data['category'],
        quantity=data['quantity']
    )
    save_product(new_product)
    response_object = {
        "Status": 'Success',
        "message": 'Successfuly added blog'
    }
    return response_object, 201


def edit_product(data):
    product = Products.query.filter_by(publicId=data['publicId']).first()
    if product:
        product.name = data['name']
        product.description = data['description']
        product.quantity = data['quantity']
        product.category = data['category']
        db.session.commmit()

        response_object = {
            'message': 'Successfuly edited product details',
            'Status': 'Successful'
        }

        return response_object, 202
    else:
        response_object = {
            'message': 'productId not found',
            'status': 'Edit Failed!'
        }
        return response_object, 235


def get_all_products():
    return Products.query.all()


def get_same_category_products(data):
    products = Products.query.filter_by(category=data['category']).all()
    return products


def search_by_name(data):
    return Products.query.filter(Products.name.startswith(data['name'])).all()


def save_product(data):
    db.session.add(data)
    db.session.commit()
