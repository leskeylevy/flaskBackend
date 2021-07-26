from flask import request
from flask_restx import Resource
from app.main.service.payments import stk_push, get_mpesa_token
from ..util.dto import MpesaDto

# from flask_mpesa import MpesaAPI

api = MpesaDto.api
mpesa = MpesaDto.product_sales


# mpesaapi = MpesaAPI

@api.route('/mpesa')
class MpesaPayment(Resource):
    """
    Mpesa payments
    """

    @api.expect(mpesa, Validate=True)
    def post(self):
        # get the post data
        data = request.json

        return stk_push(data)


@api.route('/response')
class SafaricomResponse(Resource):
    """
    Transaction response
    """

    @api.expect()
    def post(self):
        data = request.json
        return data
