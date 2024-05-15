def prime(n):
    # 1. Assume n is prime
    is_prime = True

    # 2. Test if n is prime
    for i in range(2, n):
        if n % i == 0:
            is_prime = False

    # 3. Return whether n is prime
    return is_prime