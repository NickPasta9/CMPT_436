# Nicholas Psaras, 4/10/24, CMPT-436N-111 Professor Bowu Zhang
# Below is a possible structure for your program. 
# You don't have to follow this exactly. 
# But you must have the Birthday_Paradox class with at least the indicated methods, and a main routine.

def collision(number_of_people, number_of_days):
# Input: the number_of_people at the party,
# and the number_of_days in a year, i.e., 365 for a non leap year
# Output: the probability of at least two people at the party have the same birthday 
# Complete code from here
    probability = 1.0
    for i in range(number_of_people):
        probability *= (number_of_days - i) / number_of_days
    return 1 - probability

# test case
number_of_people = 23
number_of_days = 365 
# no leap year 
print("The probability of at least two people sharing a birthday is ", collision(number_of_people, number_of_days))
# expected: Given a group of 23 people, the probability of at least two people having the same birthday is  0.5072972343239854


