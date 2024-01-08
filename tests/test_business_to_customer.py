import unittest
import sys
sys.path.insert(1, "C:/Users/user/projects/senderkash/mpesa")
from access_token import AccessToken
from business_to_customer import BusinessToCustomer
from utils import generate_security_credential
import test_variables as tv
import json

class TestBusinessToCustomer(unittest.TestCase):
	consumer_key=tv.CONSUMER_KEY
	consumer_secret=tv.CONSUMER_SECRET
	business_to_customer_url=tv.B2C_URL
	initiator=tv.INITIATOR
	party_a=tv.B2C_PARTY_A
	party_b=tv.B2C_PARTY_B
	result_url=tv.B2C_RESULT_URL
	queue_timeout_url=tv.B2C_QUEUE_TIMEOUT_URL
	token_url=tv.TOKEN_URL
	remarks=tv.B2C_REMARKS
	password=tv.PASSWORD
	command_id=tv.B2C_COMMAND_ID
	amount=tv.B2C_AMOUNT
	path=tv.CERT_PATH
	security_credentail=generate_security_credential(password,path)

	def initialize_b2c(self):
		access_token_init=AccessToken(self.consumer_key,self.consumer_secret,self.token_url)
		access_token=access_token_init.get_access_token()
		business_to_customer_init=BusinessToCustomer(access_token,self.business_to_customer_url,self.initiator,self.party_a,self.result_url,self.queue_timeout_url,self.amount,self.party_b,self.remarks,self.command_id,self.security_credentail)
		return business_to_customer_init

	def test_business_to_customer(self):
		business_to_customer_init = self.initialize_b2c()
		feedback=business_to_customer_init.business_to_customer()
		self.assertEqual(feedback['ResponseCode'],'0')

	def test_extraction_of_response(self):
		business_to_customer_init = self.initialize_b2c()
		f = open('b2c_response_test_data.json')
		data = json.load(f)
		f.close()
		feedback=business_to_customer_init.extract_response_details(data)
		print(feedback)

if __name__ == '__main__':
    unittest.main()