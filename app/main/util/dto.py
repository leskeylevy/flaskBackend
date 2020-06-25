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
