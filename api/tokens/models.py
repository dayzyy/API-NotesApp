import json
import base64
import hashlib
import hmac

class Token:
    SECRET_KEY = 'kocham192jej165oczy05'

    @classmethod
    def create_signature(cls, id, username):
        data = json.dumps({
            "username": username,
            "id": id
        })

        signature = hmac.new(
            cls.SECRET_KEY.encode('utf-8'),
            data.encode('utf-8'),
            hashlib.sha256
        ).digest()

        return signature

    @classmethod
    def issue(cls, id, username):
        data = json.dumps({
            "username": username,
            "id": id
        })

        payload = base64.urlsafe_b64encode(data.encode())
        signature = base64.urlsafe_b64encode(cls.create_signature(id, username))

        token = f'{payload.decode()}.{signature.decode()}'

        return token

def IsAuthenticated(token):
    try:
        encoded_payload, encoded_signature = token.split('.')
    except ValueError:
        return False

    payload = base64.urlsafe_b64decode(encoded_payload).decode()

    json_payload = json.loads(payload)

    expected_signature = Token.create_signature(json_payload['id'], json_payload['username'])
    encoded_signature = base64.urlsafe_b64decode(encoded_signature)

    return True if expected_signature == encoded_signature else False
