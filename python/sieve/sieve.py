import math

def sieve(n):
    A = [True] * (n+1)
    A[1] = False

    for i in range(2, n / 2): 
        j = 2 * i
        while j <= n:
            A[j] = False
            j += i

    return [m for m in range(2, n+1) if A[m]]

if __name__ == '__main__':
    print "10 = %s" % sieve(10)
    print "7 = %s" % sieve(7)
    print "1000 = %s" % sieve(1000)
    print "11 = %s" % sieve(11)

