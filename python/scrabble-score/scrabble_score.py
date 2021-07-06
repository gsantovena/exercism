def score(word):
    letter_values = {
        'aeioulnrst': 1,
        'dg': 2,
        'bcmp': 3,
        'fhvwy': 4,
        'k': 5,
        'jx': 8,
        'qz': 10,
    }

    return sum([letter_values[letters]
                for letters in letter_values.keys()
                for letter in word.lower() if letter in letters])
