for T in range(int(input())):
    n = int, input().split()
    li = list(map(int, input()))
    lst = [0] * 10

    for i in li:
        lst[i] += 1
    result = 0
    num = 0

    for i in range(10):
        if result <= lst[i]:
            result = lst[i]
            num = i
    print(f'#{T + 1} {num} {result}')
