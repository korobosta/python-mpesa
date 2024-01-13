import unittest
from transaction_query import TransactionQuery
import json

class TestTransactionQuery(unittest.TestCase):
	transaction_status_query=TransactionQuery()

	def test_transaction_status_query(self):
		response_code = None
		transaction_code = "OEI2AK4Q16"
		response=self.transaction_status_query.transaction_query(transaction_code)
		if 'ResponseCode' in response:
			response_code = response["ResponseCode"]
		self.assertEqual(response_code, '0')

	def test_extraction_of_response(self):
		f = open('transaction_query_response_test_data.json')
		data = json.load(f)
		f.close()
		feedback=self.transaction_status_query.extract_response_details(data)
		print(feedback)

if __name__ == '__main__':
	unittest.main()