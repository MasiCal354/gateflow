import hashlib
import hmac
import time
from urllib.parse import urlencode


def nonce():
    time.sleep(1 / 1000)
    return str(int(time.time() * 1000))


def signature(secret, params):
    sig = hmac.new(secret.encode(), urlencode(params).encode(), hashlib.sha512)
    return sig.hexdigest()
