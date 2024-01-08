import requests

class BusinessToCustomer:
	def __init__(self, access_token,business_to_customer_url,initiator,party_a,result_url,queue_timeout_url,amount,party_b,remarks,command_id,security_credential):
		# self.consumer_key=consumer_key
		# self.consumer_secret=consumer_secret
		self.business_to_customer_url=business_to_customer_url
		self.initiator=initiator
		self.party_a=party_a
		self.party_b=party_b
		self.result_url=result_url
		self.queue_timeout_url=queue_timeout_url
		self.command_id=command_id
		self.remarks=remarks
		self.amount=amount
		self.access_token=access_token
		self.security_credential=security_credential

	def business_to_customer(self):
		headers = {
		  'Content-Type': 'application/json',
		  "Authorization": "Bearer %s" % self.access_token
		}

		payload = {
		    "Initiator": self.initiator,
		    "SecurityCredential": self.security_credential,
		    "CommandID": self.command_id,
		    "PartyA": self.party_a,
		    "PartyB": self.party_b,
		    "Amount": self.amount,
		    "ResultURL": self.result_url,
		    "QueueTimeOutURL": self.queue_timeout_url,
		    "Remarks": self.remarks,
		    "Occassion": "",
		  }

		r = requests.get(self.business_to_customer_url, data=payload)
		json_response = r.json()
		print(json_response)
		return json_response

	def extract_response_details(self, data):
		receiver=data['Result']['ResultParameters']['ResultParameter'][4]['Value']
		split_receiver = receiver.split('-')
		phone = split_receiver[0]
		name = split_receiver[1]
		timestamp=data['Result']['ResultParameters']['ResultParameter'][5]['Value']
		amount=data['Result']['ResultParameters']['ResultParameter'][0]['Value']
		ConversationID=data['Result']['ConversationID']
		OriginatorConversationID=data['Result']['OriginatorConversationID']
		ResultCode=data['Result']['ResultCode']
		TransactionID=data['Result']['TransactionID']
		ReceiptNo=data['Result']['ResultParameters']['ResultParameter'][1]['Value']
		decoded_data = {
			'receiver_phone': phone,
			'receiver_name' : name,
			'timestamp': timestamp,
			'amount': amount,
			'ConversationID': ConversationID,
			'OriginatorConversationID' : OriginatorConversationID,
			'ResultCode' :ResultCode,
			'TransactionID' : TransactionID,
			'ReceiptNo' : ReceiptNo
		}
		return decoded_data
	    
