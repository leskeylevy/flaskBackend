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


class CommentsDto:
    api = Namespace('comments', description='comment related opreations')
    comment = api.model('comment', {
        'username': fields.String(required=True, description='username for the commenting party'),
        'comment': fields.String(required=True, description='The actual comment'),
        'blog_id': fields.Integer(required=True, description='the blog id where the comments belongs')
    })
