# Ex-8
# Read about the module random, it has method randint().
# https://docs.python.org/2/library/random.html
# Create a list with 100 random integers.
# Find out the frequency (how many times each integers is repeated in the list)
# Output should be a dictionary key as the random integer and value is the frequency
# Eg: random_integers_list = [1,2,3,4,1,3,6]
# outputs: frequencies = {1:2, 2:1, 3:2, 4: 1, 6: 1}

from random import randint
list = []
frequencies = {}
for num in range (0,100):
    list.append(randint(0,99))
for keynum in list:
    count = 0
    for num in list:
        if keynum == num:
            count = count + 1
    frequencies[keynum] = count
print list
print frequencies
