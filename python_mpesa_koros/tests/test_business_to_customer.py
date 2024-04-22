import unittest
import sys
sys.path.append("..") 
from business_to_customer import BusinessToCustomer
import json

class TestBusinessToCustomer(unittest.TestCase):
	def initialize_b2c(self):
		business_to_customer_init=BusinessToCustomer()
		return business_to_customer_init

	def test_business_to_customer(self):
		business_to_customer_init = self.initialize_b2c()
		phone_number = "254713887070"
		amount = 1
		remarks = "Send Money to Customer"
		occasion = "OK"
		feedback=business_to_customer_init.business_to_customer(phone_number,amount, remarks,occasion)
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