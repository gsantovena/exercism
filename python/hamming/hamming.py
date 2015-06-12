def distance(strand1, strand2):
    n = 0
    for a, b in zip(strand1, strand2):
        if a != b:
            n += 1
    return n

