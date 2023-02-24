"""
Write a function, is_prime, that takes a single integer parameter
and returns True when the argument is a prime number and False otherwise.
(Hint: use a web search to find out what a prime number is and how to
determine if an integer is a prime number). After that, apply
divide-and-conquer strategy by using the above function to write a program
that prints all the prime numbers, which are smaller than an integer
value provided by the user.
"""


# function to check prime number
def is_prime(n):
    """

    :param n: an integer
    :return: true if number is prime and false if number is not prime
    """
    # store all divisors into a list called div
    div = []
    for j in range(1, n+1):
        if n % j == 0:
            div.append(j)
    # if the div has more than 2 numbers then n is not a prime
    if len(div) != 2:
        return False
    else:
        return True


# main program
a = int(input())
prime = []
for i in range(1, a+1):
    if is_prime(i):
        prime.append(i)

print(prime)

# another idea:
# check from 2 to n - 1 if saw True then stop immediately (storage save)
