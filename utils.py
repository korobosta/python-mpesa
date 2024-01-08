from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5
import base64
import os


def generate_security_credential(initiator_password,certificate_path) -> str:
    """
    Generates security credentials for C2B, B2C, B2B, REVERSAL and Transaction status post requests.
    :param inititator_password: Password for the organization initiating the transaction, provided by safaricom.
    :return: string representing the security credential
    """
    bytearray_password = bytearray(initiator_password.encode('utf-8'))
    with open(certificate_path, "rb") as f:
        public_key = f.read()
    f.close()
    pub_key = RSA.importKey(public_key)
    cipher = PKCS1_v1_5.new(pub_key)

    security_credential = cipher.encrypt(bytearray_password)

    b64_encrypted = base64.b64encode(security_credential)

    security_credential = b64_encrypted.decode("utf-8")
    print(security_credential)
    return security_credential