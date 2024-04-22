#Nicholas Psaras Professor Bowu Zhang Lab 11 Cryptography 4/11/24
# Below is a possible structure for your program. 
# You don't have to follow this exactly. 
# But you must have the HMAC class with at least the indicated methods, and a main routine.

from hashlib import sha512
import base64
import hashlib

def HMAC_suffix(k, x):
# Input: a secret key k, message x
# Output: HMAC cfor the message (secret suffix MAC: h(x||k))
    x_k = x + k
    # "+" as concatenation operator to append the key k to the message x, that is, we place x before k 
    # secret suffix MAC: h(x||k)
    hmac_suffix = sha512(x_k.encode()).digest()
    return hmac_suffix


def HMAC_suffix_verify(k, x, t):
# Input: a secret key k, received message x, received HMAC t (secret suffix MAC: t= h(x||k))
# Output: true if received HMAC t matches the received message x 
    # Complete code from here
    h = hashlib.sha256()
    h.update(x.encode('utf-8'))
    h.update(k.encode('utf-8'))
    generated_hmac = h.hexdigest()
    return generated_hmac == t

def HMAC_prefix(k, x):
# Input: a secret key k, message x
# Output: HMAC cfor the message (secret prefix MAC: h(k||x))
    # Complete code from here
    h = hashlib.sha256()
    h.update(k.encode('utf-8'))
    h.update(x.encode('utf-8'))
    return h.hexdigest()


def HMAC_prefix_verify(k, x, t):
# Input: a secret key k, received message x, received HMAC t (secret prefix MAC: t= h(k||x))
# Output: true if received HMAC t matches the received message x 
    # Complete code from here
    h = hashlib.sha256()
    h.update(k.encode('utf-8'))
    h.update(x.encode('utf-8'))
    generated_hmac = h.hexdigest()
    return generated_hmac == t


# test case 1
# this a test for suffix HMAC
# Assume Alice and Bob have established a shared secret key, i.e., through DHKE. 
# Assume this secrety key is "secret key", :)
secret_key = "secret key"

# Alice wants to send a message to Bob. 
# Alice adds a HMAC (suffix) to the message. 
m = "This is a test message"
hmac_a_suffix = HMAC_suffix(secret_key, m)

print("Alice sends message: ", m, " with hmac: ", hmac_a_suffix, " to Bob.")

# Bob receives and validates the HMAC
hmac_b_verify = HMAC_suffix_verify(secret_key, m, hmac_a_suffix)

if hmac_b_verify:
  print("The message is successfully verfied.")
else:
  print("The message is corrupted. ")
  
# test case 2
# add a test case for prefix HMAC
# complete the code from here 
  
s_k = "secret_key"
x = "This is Nick Psaras"
hmac_b_prefix = HMAC_prefix(s_k, x)
print("Alice sends message: ", x, " with hmac: ", hmac_b_prefix, " to Bob.")
hmac_b_verify = HMAC_prefix_verify(s_k, x, hmac_b_prefix)

if hmac_b_verify:
  print("The message is successfully verfied.")
else:
    print("The message is corrupted. ")
    
