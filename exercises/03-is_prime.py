import math

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    return True

if __name__ == '__main__':
    state = is_prime(113)
    if state:
        print("Is a prime number")
    else:
        print("Not a prime number")
