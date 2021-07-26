from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'email': fields.String(required=True, description='user email address'),
        'username': fields.String(required=True, description='user username'),
        'public_id': fields.String(description='user Identifier'),
        'password_hash': fields.String(description='hashed password!'),
        'role': fields.String(description='user role')

    })


class AuthDto:
    api = Namespace('auth', description='Authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='username'),
        'password': fields.String(required=True, description='password'),
    })


class BlogDto:
    api = Namespace('blogs', description='Blog related operations')
    blog = api.model('blog_post', {
        'id': fields.Integer(description='Blog id'),
        'title': fields.String(required=True, description='Blog title'),
        'slug': fields.String(description='Blog slug'),
        'content': fields.String(required=True, description='Blog content'),
        'status': fields.String(required=True, description='Publish status'),
        'created_on': fields.String(description='Publishing date'),
        'caption': fields.String(required=True, description='Blog caption'),
        'author_id': fields.String(required=True, description='Author'),
        'img': fields.String(description='Blog image')
    })


class ProductDto:
    api = Namespace('products', description='Product related operations')
    product = api.model('product', {
        'name': fields.String(required=True, description='Product name'),
        'description': fields.String(required=True, description='Product description'),
        'category': fields.String(required=True, description='Product category'),
        'quantity': fields.Integer(required=True, description='Number of products available'),
        'productId': fields.String(description='Unique product identifier'),
        'supplierId': fields.String(descrpition='Unique supllier Identity'),
        'status': fields.String(description='Is it new available or out of stock?'),
        'mainImage': fields.String(description='Products main Image'),
        'angle1': fields.String(description='different angles of the product'),
        'angle2': fields.String(description='different angles of the product'),
        'angle3': fields.String(description='different angles of the product'),
        'price': fields.Integer(required=True, description='Price per product')
    })


class CommentsDto:
    api = Namespace('comments', description='comment related opreations')
    comment = api.model('comment', {
        'username': fields.String(required=True, description='username for the commenting party'),
        'comment': fields.String(required=True, description='The actual comment'),
        'blog_id': fields.Integer(required=True, description='the blog id where the comments belongs'),
        'created_on': fields.String(description='Comment created on')
    })


class MpesaDto:
    api = Namespace('mpesa', description='Mpesa operations for buying products')
    product_sales = api.model('soldProducts', {
        'phone_number': fields.String(required=True, description='Phone number making the payment'),
        'amount': fields.Integer(required=True, description='payment amount')
    })
