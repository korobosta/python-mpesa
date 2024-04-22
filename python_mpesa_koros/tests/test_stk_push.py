# from ..customer_to_business import CustomerToBusiness

import sys
sys.path.append("..")  # Add parent directory to Python path
from customer_to_business import CustomerToBusiness

import unittest

class TestStkPush(unittest.TestCase):
	def test_stk_push(self):
		response_code = None
		amount = 1
		phone = "254713887070"
		bill_reference = "TYJ667"
		customer_to_business=CustomerToBusiness()
		repsonse=customer_to_business.stk_push(amount,phone,bill_reference)
		if 'ResponseCode' in repsonse:
			response_code = repsonse["ResponseCode"]
		self.assertEqual(response_code, '0')

if __name__ == '__main__':
    unittest.main()