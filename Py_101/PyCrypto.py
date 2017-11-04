# pip install pycryptodome
# pip install pycryptodomex
from Crypto.Cipher import DES, RSA


# encrypting a string
key = b'abcdefgh'


def pad(text):
    while len(text) % 8 != 0:
        text += b' '
    return text


des = DES.new(key, DES.MODE_ECB)
text = b'Python rocks!'
padded_text = pad(text)
encrypted_text = des.encrypt(text)
encrypted_text = des.encrypt(padded_text)


# create an RSA key
code = 'nooneknows'
key = RSA.generate(2048)
encrypted_key = key.exportKey(passphrase=code, pkcs=8,
                              protection="scryptAndAES128-CBC")


with open('/path_to_private_key/my_private_rsa_key.bin', 'wb') as f:
    f.write(encrypted_key)


with open('/path_to_public_key/my_rsa_public.pem', 'wb') as f:
    f.write(key.publickey().exportKey())


# encrypting a file


# the cryptography package
