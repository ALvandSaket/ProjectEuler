# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

TARGET = 2000000


def if_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


nums = []
total = 3

for i in range(3, TARGET, 2):
    if if_prime(i):
        total += i

print(total)
