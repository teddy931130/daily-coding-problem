numbers = list(map(int, input().split()))
k = int(input())

for x in range(len(numbers)):
    for y in range(len(numbers)):
        if y == x:
            continue
        if numbers[x] + numbers[y] == k:
            print(True)
            exit(0)

print(False)
