from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.auth_controller import api as auth_ns
from .main.controller.blog_controller import api as blog_ns
from .main.controller.comments_controller import api as comments_ns
from .main.controller.product_controller import api as products_ns
from .main.controller.mpesa_payment_controller import api as mpesa_ns
blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTX API BOILER-PLATE WITH JWT',
          version='1.0',
          description='a boilerplate for flask restx web service'
          )

api.add_namespace(user_ns, path='/user')
api.add_namespace(auth_ns)
api.add_namespace(blog_ns, path='/blogs')
api.add_namespace(comments_ns, path='/comments')
api.add_namespace(products_ns, path='/products')
api.add_namespace(mpesa_ns, path='/mpesa')
