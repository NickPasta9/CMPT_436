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


#ECB mode
ecb_cipher = AES.new(key, AES.MODE_ECB)
ecb_cipher_text = ecb_cipher.encrypt(pad(data, AES.block_size))


# change one char in plaintext
m_ecb_cipher = AES.new(key, AES.MODE_ECB)
m_ecb_cipher_text = m_ecb_cipher.encrypt(pad(mdata, AES.block_size))


print("ecb mode ciphertext: \n", ecb_cipher_text.hex())
print("ecb mode ciphertext (with one char error in plaintext): \n", m_ecb_cipher_text.hex())


# Compare two ciphertexts and get differences
print("Differences between two ciphertexts: ")
differ = difflib.Differ()
diff = list(differ.compare(ecb_cipher_text.hex(), m_ecb_cipher_text.hex()))
print("".join(diff))



ecb_decrypt_cipher = AES.new(key, AES.MODE_ECB)
ecb_plaintext = ecb_decrypt_cipher.decrypt(ecb_cipher_text)
print("ecb mode decrypted plaintext: \n", unpad(ecb_plaintext, AES.block_size))

m_decrypt_cipher = AES.new(key, AES.MODE_ECB)
m_plain_text = m_decrypt_cipher.decrypt(m_ecb_cipher_text)
print("ecb mode decrypted plaintext (with one char error in plaintext): \n", unpad(m_plain_text, AES.block_size))