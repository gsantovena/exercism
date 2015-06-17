def slices(string, n):
    if n > len(string) or n == 0:
        raise ValueError("Slice's size should be less than the string length.")

    slices_list = []
    for i in range(0, len(string) - n + 1):
        one_slice = []
        for j in range(i, i + n):
            one_slice.append(int(string[j:j+1]))

        slices_list.append(one_slice)

    return slices_list

if __name__ == '__main__':
    print slices("97867564", 3)
    print slices("012", 4)

