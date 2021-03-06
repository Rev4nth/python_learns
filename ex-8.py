# Ex-10
# Write a function isPrime, that takes a number as argument.
# Returns true if it is a prime number, false if it is not.
# Eg: is_prime(20) -> False, is_prime(13) -> True

def is_prime(num):
    count = 0
    for divisors in range(1, num/2):
        if num % divisors == 0:
            count = count + 1
    if count == 1:
        print "%d is a prime" %(num)
    else:
        print "%d is not a prime" %(num)

is_prime(11)
is_prime(19)
