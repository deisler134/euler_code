def check_prime(n:int)->bool:
    if n < 1:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i*i <= n:
        if n % i == 0 or n % (i+2) == 0:
            return False
        i += 6
    return True

if __name__ == "__main__":
    n = 104743
    if check_prime(n): print('{0} is prime'.format(n))
    else : print('{0} is not prime'.format(n))
    