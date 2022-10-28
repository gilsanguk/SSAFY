for T in range(int(input())):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    min_v = 1000001
    max_v = 0
    for i in range(n-m+1):
        tmp = 0
        for j in range(i, i + m):
            tmp += li[j]
        if tmp > max_v:
            max_v = tmp
        if tmp < min_v:
            min_v = tmp
    print(f'#{T + 1} {max_v - min_v}')
