def is_anagram(word, anagram):
    if word.lower() == anagram.lower():
        return False

    word_list = list(word.lower())
    word_list.sort()
    anagram_list = list(anagram.lower())
    anagram_list.sort()

    return word_list == anagram_list

def detect_anagrams(word, anagrams):
    anagrams_list = []
    for w in anagrams:
        if is_anagram(word, w):
            anagrams_list.append(w)

    return anagrams_list


if __name__ == '__main__':
    detect_anagrams('ant', 'tan stand at'.split())

