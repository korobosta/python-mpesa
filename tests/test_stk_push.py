from customer_to_business import CustomerToBusiness

import unittest

class TestStkPush(unittest.TestCase):
	def test_access_token(self):
		response_code = None
		amount = 1
		phone = "254713887070"
		customer_to_business=CustomerToBusiness()
		repsonse=customer_to_business.stk_push(amount,phone)
		if 'ResponseCode' in repsonse:
			response_code = repsonse["ResponseCode"]
		self.assertEqual(response_code, '0')

if __name__ == '__main__':
    unittest.main()