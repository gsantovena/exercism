def prime_factors(n):
    factors = []
    prime = 2

    while n > 1:
        while n % prime == 0:
            factors.append(prime)
            n /= prime

        prime += 1
        
    return factors

if __name__ == '__main__':
    print(prime_factors(60))

