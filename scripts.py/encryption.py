import pyaes, pbkdf2, binascii, os, secrets
import urllib.request

# Encrypt the plaintext with the given key:
#   ciphertext = AES-256-CTR-Encrypt(plaintext, key, iv)
password = "blos123"
passwordSalt = os.urandom(16)
key = pbkdf2.PBKDF2(password, passwordSalt).read(32)
iv = secrets.randbits(256)
URL =  "http://127.0.0.1:8000/chunks/the-amazing-spiderman%20"
aes = pyaes.AESModeOfOperationCTR(key, pyaes.Counter(iv))
ciphertext = aes.encrypt(URL)
print('Encrypted:', binascii.hexlify(ciphertext))
decrypted = aes.decrypt(ciphertext)
print('Decrypted:', decrypted)
