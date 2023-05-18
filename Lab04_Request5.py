#NT213.N21.ANTT
import base64
from Crypto.Cipher import AES

class CryptoClass:
    def __init__(self):
        self.base64Text = ""
        self.cipherData = b""
        self.ivBytes = b"\x00" * 16 # 16 bytes of zeros
        self.key = b"This is the super secret key 123" # convert to bytes
        self.plainText = ""

    @staticmethod
    def aes256decrypt(iv, key, data):
        cipher = AES.new(key, AES.MODE_CBC, iv)
        return cipher.decrypt(data)

    def aesDeccryptedString(self, text):
        self.cipherData = self.aes256decrypt(self.ivBytes, self.key, base64.b64decode(text))
        self.plainText = self.cipherData.decode("utf-8") # convert to string
        return self.plainText

    def DecryptedOutput(self, text):
        return self.aesDeccryptedString(text)

def main():
    # create an instance of CryptoClass
    crypto = CryptoClass()
    print("Enter the encrypted username:")
    username_cipher_text = input()
    print("Enter the encrypted password:")
    password_cipher_text = input()
    
    # call the DecryptedOutput function with the ciphertext
    print("Username: " + base64.b64decode(username_cipher_text).decode("utf-8"))
    print("Password: " + crypto.DecryptedOutput(password_cipher_text))

if __name__ == "__main__":
    main()
