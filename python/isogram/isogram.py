def is_isogram(string):
    valid_chars = list(map(chr, range(97, 123)))
    s = string.lower()

    return len([x for x in s if s.count(x) > 1 and x in valid_chars]) == 0
