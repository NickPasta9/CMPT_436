# Below is a possible structure for your program. 
# You don't have to follow this exactly. 
# But you must have the RSA digital signature class with at least the indicated methods, and a main routine.

def sign(message, d, n):
    signature = pow(message, d, n)
    return signature
    
# Input: the message Alice wants to send, and Alice's key
# Which key does Alice use to sign her message?
# Output: signature
# Complete code from here
  
  
def verify(signature, e, n):
    verification = pow(signature, e, n)
    return verification
    
  #verification = pow(signature, e, n)
  #return verification
  
# Input: the message and the signature Bob recieves, and Alice's key
# Which key does Bob use to verify Alice's message?
# Output: true if the message is from Alice, false otherwise
# Complete code from here
  


# Test case
# Assume we have already executed RSA,
# and generated the following keys for Alice:
# Public key (e, n): 5, 170171
# Secret key (d) 9677

n = 170171
e = 5
d = 9677

# This is the message that Alice wants to sign and send to Bob
message = 20

# Step 1: create signature (use Alice's private key)
# In real world applications, a message is often longer than RSA keys. 
# In practice, we are supposed to hash the message first -- shorten the message, then sign its hashed value.
# Hash functions will be discussed later in the class.  
# In this program, we use "Textbook" RSA digital signature, and assume all messages are short, less than RSA keys, so that we do NOT need hash.
# For example, message = 20, definitely less than the key.
# We can sign the short message directly without hash. 
sig = sign(message, d, n)

# Step 2: send message with signature to Alice
print("Alice sends message: ", message, " with signature: ", sig, " to Bob.")


# Bob verifies the signature


# Step 1: Verify the signature (use Alice's public key)
verification = verify(sig, e, n)

print("Verification value from the signature", verification)

if message == verification:
  print("The message is successfully verfied.")
else:
  print("The message does NOT match the signature. The message is corrupted. ")


# This is Eve being evil and modifies the message

m_modified = 10
# modify the message

print("Modified message: ",m_modified)

# Assume Bob receives the modified message

# Alice verifies the signature
# Step 1: Verify the signature (use Alice's public key)
verification = verify(sig, e, n)
print("Verification value", verification)
if verification != m_modified:
    print("Message has been modified")
else:
    print("Verification correct")

