class Luhn(object):
	
    def __init__(self, number):
        self.number = number

    def addends(self):
        def digits_of(n):
            return [int(d) for d in str(n)]

        digits = digits_of(self.number)

        return [sum(digits_of(n*2)) if i % 2 == 0 else n
            for i, n in enumerate(digits, start=len(digits) % 2)]

    def checksum(self):
        return sum(self.addends()) % 10

    def is_valid(self):
        return self.checksum() == 0

    def create(n):
        check_digit = Luhn(n * 10).checksum()
        return int(str(n) + str(check_digit if check_digit == 0 else 10 - check_digit))

    create = staticmethod(create)
		
if __name__ == '__main__':
        print(Luhn(12121).addends())
        print(Luhn(8631).addends())


