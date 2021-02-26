def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    state = is_prime(7)
    if state:
        print("Is a prime number")
    else: 
        print("Not a prime number")