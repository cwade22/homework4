# create  prime number function
def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        for test in range (2,n):
            if (n % test ) == 0:
                return False
        return True
# create random function
def random():
    import random
    r1 = random.randint(1,100)
    r2 = random.randint(1,100)
    r3 = random.randint(1,100)
    r4 = random.randint(1,100)
    r5 = random.randint(1,100)
    r6 = random.randint(1,100)

    if is_prime(r1):
        print('The random number', r1, 'is a prime number.')
    else:
        print('The random number', r1, 'is not a prime number.')
    if is_prime(r2):
        print('The random number', r2, 'is a prime number.')
    else:
        print('The random number', r2, 'is not a prime number.')
    if is_prime(r3):
        print('The random number', r3, 'is a prime number.')
    else:
        print('The random number', r3, 'is not a prime number.')
    if is_prime(r4):
        print('The random number', r4, 'is a prime number.')
    else:
        print('The random number', r4, 'is not a prime number.')
    if is_prime(r5):
        print('The random number', r5, 'is a prime number.')
    else:
        print('The random number', r5, 'is not a prime number.')
    if is_prime(r6):
        print('The random number', r6, 'is a prime number.')
    else:
        print('The random number', r6, 'is not a prime number.')
random()

