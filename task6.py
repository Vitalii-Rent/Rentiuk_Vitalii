def next_bigger(num):
    digits = list(str(num))
    i = len(digits) - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1

    if i == -1:
        return -1

    j = len(digits) - 1
    while j > i and digits[j] <= digits[i]:
        j -= 1

    digits[i], digits[j] = digits[j], digits[i]
    digits[i + 1:] = reversed(digits[i + 1:])
    return int(''.join(digits))