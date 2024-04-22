#Nicholas Psaras Lab 7 Professor Bowu Zhang Due Date: March 5th 
# Below is a possible structure for your program. 
# You don't have to follow this exactly. 
# But you must have the SquareMultiply class with at least the indicated methods, and a main routine.


import sys


def squaremultiply(base, exponent):
    # input: x, y
    # output: x^y using square and multiply

    exp = bin(exponent)
    # save the binary bits of exponent b in exp[]
    result = base
    
    
    for i in range(3, len(exp)): 
    # Scan the exponent bits in exp[] one by one.
    # Ignore the first bit in the exponent bits.
    # Skip the prefix "0b" (index 0, 1 in exp[]), then the first bit of exponent (index 2).
    # As a result, in exp[], start from index 3
    # complete code from here
        result *= result
        if exp [i] == '1':
            result *= base
            
    return result



print ("We will calculate a^b")
a=2
b=4
print ("a=",a)
print ("b=",b)
print ("==== Calculation ====")
res=squaremultiply(a,b)
print ("Result:",res)

print (")===========")