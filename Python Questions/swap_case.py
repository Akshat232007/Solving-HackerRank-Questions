def swap_case(s):
    split_char = [char for char in s]
    left = 0

    while left < len(split_char):
        if split_char[left].islower():
            split_char[left] = split_char[left].upper()
        else:
            split_char[left] = split_char[left].lower()

        left = left + 1
    sentence = "".join(split_char)
    return sentence


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)