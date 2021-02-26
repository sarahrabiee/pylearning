def is_prime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                return False
        return True
    return false

if __name__ == '__main__':
    state = is_prime(67)
    if state:
        print("Is a prime number")
    else: 
        print("Not a prime number")