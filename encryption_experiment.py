
from Crypto.Cipher import AES

# 16 characters long
iv = "1234567890123456"
# 32 characters long
key = "12345678901234567890123456789012"

AES_CIPHER = AES.new(key, AES.MODE_CFB, IV=iv)

def encrypt(string):
    return AES_CIPHER.encrypt(string)

def decrypt(bytez):
    return AES_CIPHER.encrypt(bytez)

def main():
    input_string = "this is the string to be encrypted"
    encrypted = encrypt(input_string)
    decrypted = decrypt(encrypted)
    print("result is " + decrypted)

if __name__ == "__main__":
    main()
