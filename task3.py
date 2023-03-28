def digital_root(num: int):
    while num > 10:
        print(num)
        num = recursion(num)
    return num


def recursion(num: int):
    if num < 10:
        return num
    x = num % 10
    return x + recursion((num - x) // 10)