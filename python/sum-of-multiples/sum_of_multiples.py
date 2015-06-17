def sum_of_multples_cbyn(num, mult = [3, 5]):
    return sum(set(n for n in range(1, num) for m in mult if m and not n % m))

def sum_of_multiples(n, factors = [3, 5]):
    result = 0
    for m in range(1, n):
        for f in factors:
            if f != 0 and m % f == 0:
                result += m
                break

    return result

if __name__ == '__main__':
    print sum_of_multiples(1)
    print sum_of_multiples(1000)
    print sum_of_multiples(20, [7, 13, 17])

