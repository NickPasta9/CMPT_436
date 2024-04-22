import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
import base64
import difflib


def base64Encoding(input):
  dataBase64 = base64.b64encode(input)
  dataBase64P = dataBase64.decode("UTF-8")
  return dataBase64P

def base64Decoding(input):
    return base64.decodebytes(input.encode("ascii"))



data = b'0123456789 012340123456789 012340123456789 012340123456789 01234'
mdata= b'0123456789 012340123456789 412340123456789 012340123456789 01234'

#encryption
key = get_random_bytes(16)
# or you can set AES_KEY=MbQeThWmZq4t6w9z


#CBC mode
cbc_cipher = AES.new(key, AES.MODE_CBC)
cbc_cipher_text = cbc_cipher.encrypt(pad(data, AES.block_size))
iv = cbc_cipher.iv


# change one char in plaintext
m_cbc_cipher = AES.new(key, AES.MODE_CBC, iv=iv)
m_cbc_cipher_text = m_cbc_cipher.encrypt(pad(mdata, AES.block_size))

print("cbc mode ciphertext: ", cbc_cipher_text.hex())
print("cbc mode ciphertext (with one char error in plaintext): ", m_cbc_cipher_text.hex())




# Compare ciphertexts and get differences
differ = difflib.Differ()
diff = list(differ.compare(cbc_cipher_text.hex(), m_cbc_cipher_text.hex()))
print("Differences between two ciphertexts: ")
print("".join(diff))




#decryption
cbc_decrypt_cipher = AES.new(key, AES.MODE_CBC, iv=iv)
cbc_plaintext = cbc_decrypt_cipher.decrypt(cbc_cipher_text)
print("cbc mode decrypted plaintext: ", unpad(cbc_plaintext, AES.block_size))




m_decrypt_cipher = AES.new(key, AES.MODE_CBC, iv=iv)
m_plain_text = m_decrypt_cipher.decrypt(m_cbc_cipher_text)
print("cbc mode decrypted plaintext (with one char error in plaintext): ", unpad(m_plain_text, AES.block_size))



