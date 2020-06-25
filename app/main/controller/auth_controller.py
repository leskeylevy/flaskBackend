from flask import request
from flask_restx import Resource

from app.main.service.auth_helper import Auth
from ..util.dto import AuthDto

api = AuthDto.api
user_auth = AuthDto.user_auth


@api.route('/login')
class UserLogin(Resource):
    """
    User Login Resource
    """

    @api.expect(user_auth, Validate=True)
    @api.doc('Login User')
    def post(self):
        # get the post data
        data = request.json
        username = data['username']
        password = data["password"]
        post_data = {
            'username': username,
            'password': password
        }
        return Auth.login_user(data=post_data)
        # return post_data


@api.route('/logout')
class LogoutAPI(Resource):
    """
    Logout Resource
    """

    @api.doc('logout a user')
    def post(self):
        # get auth token
        # access_token = request.hea.get('access_token')
        auth_header = request.headers.get('access_token')
        return Auth.logout_user(data=auth_header)
