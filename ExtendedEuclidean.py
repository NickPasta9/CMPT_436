def egcd(a, b):
    # Extended Euclidean algorithm
    # input: a, b, a < b
    # output: gcd(a, b), and x, y such that 
    # gcd(a, b) = a * x + b * y 
    # base-case
    # gcd(0, b)=b and a * x + b * y = b, so x = 0 and y = 1
    if a == 0:
        return b, 0, 1

    # use the Euclidean algorithm for gcd()
    # b%a is always the smaller number - and 'a' is the smaller integer
    gcd, x1, y1 = egcd(b % a, a)

    # and we update the parameters for x, y accordingly
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y

def inverse(a, b):
# compute the inverse of a mod b
# note that the inverse of a exists only if gcd(a, b) = 1
    return egcd(a, b)[1]


# Test case
a, b =3, 20
g, x, y = egcd(a, b)
# print(egcd(a, b))
print("gcd(", a, ",", b, ") = ", g)
print("The inverse of " + str(a) + " mod " + str(b) + " is " + str(x))