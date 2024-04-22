# Below is a possible structure for your program. 
# You don't have to follow this exactly. 
# But you must have the Diffie-Hellman key exchange class with at least the indicated methods, and a main routine.

import math
import random

def is_prime(p):
# Examine if a given number p is prime
    for i in range(2, int(math.sqrt(p))):

        if p % i == 0:
            return False
    return True


def get_prime(size):
# Find a prime number p
    while True:
        p = random.randrange(size, 2*size)
        if is_prime(p):
            return p


def is_generator(g, p):
# Examine if a given number g is a generator of Z^*_p
    for i in range(1, p - 1):
        if (g**i) % p == 1:
            return False
    return True


def get_generator(p):
# Create a generator g of Z^*_p
    for g in range(2, p):
        if is_generator(g, p):
            return g



def generate_secret_key(g, p):
# Input: public parameters: g (generator, base), p (modulus)
# Output: shared secret key using Diffie-Hellman Key Exchange
    # Alice
    a = random.randrange(0, p-1)
    # Alice private key a
    A = (g**a) % p
    # Alice public key A

    # Alice publishes A in the public
    print("Alice public key: A ", A)
    
    # Complete code from here
    b = random.randrange(0, p-1)
    #Bob public key b
    B = (g**b) % p
    print("Bob public key: B ", B)    
    
    #Alice shared secret key 
    sk_Alice = (B**a) % p
    print("Alice secret key: ", sk_Alice)
    #Bob shared secret key = Alice shared secret key 
    sk_Bob = (A**b) % p
    print("Bob secret key: ", sk_Bob)

# test case
# Alice and Bob agree on public parameters g, p
p = get_prime(10000)
g = get_generator(p)
# Print public parameters g, p
print(g, p)
# Create shared secret key using Diffie-Hellman Key Exchange 
generate_secret_key(g, p)