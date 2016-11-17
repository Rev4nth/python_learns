# Ex-11
# Mutable vs Immutable data types
# Follow this video https://www.youtube.com/watch?v=5qQQ3yzbKp8
# Label the following datatypes whether they are mutable or immutable
# String
# List
# Dictionary
# Tuple

# String and tuple is immutable
# List and Dictionary is mutable

def nthprime(num):
    nth = 2
    eachNum = 2
    while nth != num:
        count = 0
        print eachNum
        for divisors in range(1,eachNum):
            if num % divisors == 0:
                count = count + 1
        print eachNum
        if count == 1:
            nth = nth+1
    print eachNum

nthprime(4)
