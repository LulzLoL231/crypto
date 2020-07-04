# crypto – cleartext + JWT + lulzcode = simple way for some encrypting.
Encrypt cleartext by JWT, encode it with lulzcode, and upload it to pastebin.

## Dependence?
Python =<3.7
JWT
requests
lulzcode
pastebin API key (optional)

## How to use?
```python
from crypto import Crypto

enc = Crypto('<SUPER_SECRET_PASSWORD>', '<PASTEBIN_API_KEY>')

enc.encrypt('Hello World!')  # Output: https://pastebin.com/irLbQN3g

enc.decrypt('irLbQN3g')  # Output: Hello World!```
