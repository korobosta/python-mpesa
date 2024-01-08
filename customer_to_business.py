import base64
import datetime
import requests
import os
from dotenv import load_dotenv
from access_token import AccessToken
load_dotenv()


class CustomerToBusiness:	
	def stk_push(self,amount, phone):
		time = datetime.datetime.now()
		timestamp = time.strftime('%Y%m%d%H%M%S')
		data = os.getenv('MPESA_BUSINESS_SHORTCODE') + os.getenv('MPESA_PASSKEY') + timestamp
		encoded_string = base64.b64encode(data.encode())
		password = encoded_string.decode('utf-8')
		callback_url = os.getenv('MPESA_CALLBACK_URL')
		token = AccessToken()
		access_token=token.get_access_token()
		api_url = os.getenv('CUSTOMER_TO_BUSINESS_URL')
		headers = { "Authorization": "Bearer %s" % access_token }
		request = {
            "BusinessShortCode": os.getenv('MPESA_BUSINESS_SHORTCODE'),
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": os.getenv('MPESA_BUSINESS_SHORTCODE'),
            "PhoneNumber": phone,
            "CallBackURL": callback_url,
            "AccountReference": phone,
            "TransactionDesc": " Product Online Purchase"
        }
		response = requests.post(api_url, json = request, headers=headers)
		json_response = response.json()
		print(json_response)
		return (json_response)
	    
