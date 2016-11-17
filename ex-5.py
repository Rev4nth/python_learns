# Ex-6
# Read about the module random, it has method randint().
# https://docs.python.org/2/library/random.html
# Create a list with 100 random integers.

from random import randint
for randomNumber in range(1,100):
    print 'Random number %d  is %d' %(randomNumber, randint(200,300))
