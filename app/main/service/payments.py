import os
import requests
from requests.auth import HTTPBasicAuth
import json
import base64
import datetime

unformatted_time = datetime.datetime.now()
formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")
# print(formatted_time)
business_short_code = '174379'
shortCode = '174379'
lipa_na_mpesa_passkey = 'bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919'
data_to_encode = business_short_code + lipa_na_mpesa_passkey + formatted_time
encoded_string = base64.b64encode(data_to_encode.encode())

decoded_password = encoded_string.decode('utf-8')


# print(lipa_na_mpesa_passkey, business_short_code)

def get_mpesa_token():
    consumer_key = os.getenv('consumer_key')
    consumer_secret = os.getenv('consumer_secret')
    api_Url: str = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_Url, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    return r.json()['access_token']


# noinspection PyBroadException
def stk_push(data):
    """ make stk push to daraja API"""

    # make stk push

    # get access_token
    access_token = get_mpesa_token()

    # stk_push request_url

    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    # put access_token in header
    headers = {"Authorization": "Bearer %s" % access_token}

    # request body
    request = {
        "BusinessShortCode": business_short_code,
        "Password": decoded_password,
        "Timestamp": formatted_time,
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "1",
        "PartyA": +254716578738,
        "PartyB": business_short_code,
        "PhoneNumber": +254716578738,
        "CallBackURL": "https://5f708ec1407d.ngrok.io/mpesa/response",
        "AccountReference": "ronchez fitness inc.",
        "TransactionDesc": "Payment for goods"
    }
    response = requests.post(api_url, json=request, headers=headers)
    return response.text


# def c2b_transaction():
#     access_token = get_mpesa_token()
#     api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
#     headers = {"Authorization": "Bearer %s" % access_token}
#     request = {
#         "shortCode": shortCode,
#         "ResponseType": 'Completed',
#         "ConfirmationURL": "https://56c26501772c.ngrok.io/mpesa/confirm",
#         "ValidationURL": "https://56c26501772c.ngrok.io/mpesa/response"
#         }
#     response = requests.post(api_url, json=request, headers=headers)
#     return response.text

# function to register confirmation and validation url



