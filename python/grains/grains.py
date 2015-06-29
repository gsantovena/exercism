def on_square(n):
	return 2 ** (n-1)
	
def total_after(n):
	return sum([on_square(x) for x in xrange(1, n+1)])
	
if __name__ == '__main__':
	print(on_square(2))
	print(total_after(2))
	
	print(on_square(64))
	print(total_after(64))
	