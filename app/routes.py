from flask import Blueprint, jsonify, request
from .models import Product
from . import db

api_bp = Blueprint('api', __name__, url_prefix='/api')

@api_bp.route('/products', methods=['GET'])
def get_products():
    products = Product.query.all()
    return jsonify([product.to_dict() for product in products])

@api_bp.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = Product(
        name=data.get('name'),
        price=data.get('price'),
        quantity=data.get('quantity')
    )
    db.session.add(new_product)
    db.session.commit()
    return jsonify(new_product.to_dict()), 201

@api_bp.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    product = Product.query.get_or_404(id)
    data = request.json
    product.name = data.get('name', product.name)
    product.price = data.get('price', product.price)
    product.quantity = data.get('quantity', product.quantity)
    db.session.commit()
    return jsonify(product.to_dict())

@api_bp.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = Product.query.get_or_404(id)
    db.session.delete(product)
    db.session.commit()
    return jsonify({"message": "Product deleted successfully"})
