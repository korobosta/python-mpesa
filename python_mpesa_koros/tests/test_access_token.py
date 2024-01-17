from access_token import AccessToken

import unittest

class TestAccessToken(unittest.TestCase):
	def test_access_token(self):
		a_t=AccessToken()
		token=a_t.get_access_token()
		self.assertIsNotNone(token)

if __name__ == '__main__':
    unittest.main()