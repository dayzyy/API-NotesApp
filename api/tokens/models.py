import json
import base64
import hashlib
import hmac
from urllib import parse

class Token:
    SECRET_KEY = 'kocham192jej165oczy05'

    @classmethod
    def create_signiture(cls, id, username):
        data = json.dumps({
            "username": username,
            "id": id
        })

        signiture = hmac.new(
            cls.SECRET_KEY.encode('utf-8'),
            data.encode('utf-8'),
            hashlib.sha256
        ).digest()

        return signiture

    @classmethod
    def issue(cls, id, username):
        data = json.dumps({
            "username": username,
            "id": id
        })

        payload = base64.urlsafe_b64encode(data.encode())
        signiture = cls.create_signiture(id, username)

        payload = parse.quote(payload)
        signiture = parse.quote(signiture)

        token = f'{payload}.{signiture}'

        return token

def IsAuthenticated(token):
    encoded_payload, encoded_signiture = token.split('.')

    encoded_payload = parse.unquote(encoded_payload)
    payload = base64.urlsafe_b64decode(encoded_payload).decode()

    json_payload = json.loads(payload)

    expected_signiture = Token.create_signiture(json_payload['id'], json_payload['username'])
    encoded_expected_signiture = parse.quote(expected_signiture)

    return True if encoded_expected_signiture == encoded_signiture else False
