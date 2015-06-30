def transform(text):
    return {letter.lower(): points for points, letters in text.items() for letter in letters}

if __name__ == '__main__':
    print transform('WORLD')

