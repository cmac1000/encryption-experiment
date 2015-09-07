import os
import base64
from Crypto.Cipher import AES

# 16 characters long
iv = "1234567890123456"
# 32 characters long
key = "12345678901234567890123456789012"

AES_CIPHER = AES.new(key)

BLOCK_SIZE = 32
PADDING='@'

# https://gist.githubusercontent.com/mohsinhijazee/07cdfc2826a565b50a68/raw/39b81ac6bed3af17b28f62df64f21188771f42d5/encdec.py

def _pad(data, pad_with=PADDING):
    """
    Data to be encrypted should be on 16, 24 or 32 byte boundaries.
    So if you have 'hi', it needs to be padded with 30 more characters
    to make it 32 bytes long. Similary if something is 33 bytes long,
    more bytes are to be added to make it 64 bytes long which falls
    32 boundaries.
    BLOCK_SIZE is the boundary to which we round our data to.
    PADDING is the character that we use to padd the data.
    """
    return data + (BLOCK_SIZE - len(data) % BLOCK_SIZE) * PADDING

def encrypt(string):
    cipher = AES.new(_pad(key, '#')[:32])
    return base64.b64encode(cipher.encrypt(_pad(string)))

def decrypt(bytez):
    cipher = AES.new(_pad(key, '#')[:32])
    return cipher.decrypt(base64.b64decode(bytez)).rstrip(PADDING)

def main():
    input_string = "this is the string to be encrypted"
    encrypted = encrypt(input_string)
    decrypted = decrypt(encrypted)
    print("result is " + decrypted)

if __name__ == "__main__":
    main()
