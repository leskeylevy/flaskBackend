import flask
from flask_restx import Resource

from ..util.dto import ProductDto
from ..service.product_service import save_new_product, get_all_products, get_same_category_products, search_by_name, \
    edit_product, delete_product, search_by_id

api = ProductDto.api
_product = ProductDto.product


@api.route('/')
class ProductList(Resource):
    @api.doc('list_of_all_products')
    @api.marshal_list_with(_product, envelope='data')
    def get(self):
        """List all products"""
        return get_all_products()


@api.route('/<category>')
@api.param('category', 'Product Category')
@api.response(404, 'Category does not exist')
class CategoryProducts(Resource):
    @api.doc('list_of_all_products_under_one_category')
    @api.marshal_with(_product)
    def get(self, category):
        """List all product under queried category"""
        products = get_same_category_products(category)
        if not products:
            api.abort(404)
        else:
            return products


@api.route('/all/<name>')
@api.param('name', 'Product Name')
@api.response(404, 'Product not found')
class Product(Resource):
    @api.doc('Products with that name')
    @api.marshal_with(_product)
    def get(self, name):
        """Products with that name"""
        products = search_by_name(name)
        return products


@api.route('/one/<productid>')
@api.param('productid', 'Product id')
@api.response(404, 'Product not found')
class Product(Resource):
    @api.doc('A single product with the given Id')
    @api.marshal_with(_product)
    def get(self, productid):
        """Products with that name"""
        products = search_by_id(productid)
        return products


@api.route('/addProduct')
@api.response(200, "product added")
class AddProduct(Resource):
    @api.doc('Create new product')
    @api.expect(_product, validate=True)
    def post(self):
        """Creates Product"""
        data = flask.request.json
        return save_new_product(data)


@api.route('/editProduct')
@api.response(200, "Product edited")
class EditProduct(Resource):
    @api.doc('Edit a Product')
    @api.expect(_product, validate=True)
    def post(self):
        """Updates product"""
        data = flask.request.json
        return edit_product(data)


@api.route('/delete/<productid>')
@api.param('productid', 'Product Id')
@api.response(200, "Product deleted")
class DeleteProduct(Resource):
    @api.doc('Delete a Product')
    @api.marshal_with(_product)
    def delete(self, productid):
        """Delete a product"""
        return delete_product(productid)
