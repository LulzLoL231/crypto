# LulzCrypto

LulzCrypto – Simple way for some encrypting.

Encrypt cleartext by JWT, encode it with lulzcode, and upload it to pastebin.

## How to install?

```sh
pip install lulzcrypto
```

## Dependence?

Python >=3.7

JWT

requests

lulzcode

pastebin API key (optional)

## How to use?

With pastebin upload.
```python
from lulzcrypto import Crypto

enc = Crypto('<SUPER_SECRET_PASSWORD>', '<PASTEBIN_API_KEY>')

enc.encrypt('Hello World!')  # Output: https://pastebin.com/irLbQN3g
enc.decrypt(pastebin='irLbQN3g')  # Output: Hello World!
```

With just encrypting.
```python
from lulzcrypto import Crypto

enc = Crypto('<SUPER_SECRET_PASSWORD>')

enc.encrypt('Hello World!')  # Output: 332567151533411...1616
enc.decrypt(text='332567151533411...1616')  # Output: Hello World!
```

## Where get pastebin API key?
Just visit https://pastebin.com, sign up, and visit https://pastebin.com/api#1
