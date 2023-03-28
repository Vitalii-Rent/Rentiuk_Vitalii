def count_pairs_with_sum(arr, target):
    count = 0
    seen = set()

    for num in arr:
        complement = target - num
        if complement in seen:
            count += 1
        seen.add(num)

    return count