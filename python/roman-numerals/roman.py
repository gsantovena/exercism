roman_numbers = {
    1: 'I',
    4: 'IV',
    5: 'V',
    9: 'IX',
    10: 'X',
    40: 'XL',
    50: 'L',
    90: 'XC',
    100: 'C',
    400: 'CD',
    500: 'D',
    900: 'CM',
    1000: 'M',
}

def numeral(arabic):
    s = ''
    for n, r in reversed(sorted(roman_numbers.items())):
        while arabic >= n:
            s += r
            arabic -= n

    return s

if __name__ == '__main__':
    print(numeral(2015))
    print(numeral(1979))
    print(numeral(1948))
    print(numeral(1956))



