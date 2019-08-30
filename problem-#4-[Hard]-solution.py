def missing_positive_int(n):
    lowest = 1
    n = [num for num in n if num > 0]

    for num in sorted(n):
        if num == lowest:
            lowest += 1

    print(lowest)


numbers = list(map(int, input().split()))
missing_positive_int(numbers)
