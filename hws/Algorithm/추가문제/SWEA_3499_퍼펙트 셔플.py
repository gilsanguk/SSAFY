for T in range(int(input())):
    n = int(input())
    li = list(input().split())
    res = [0] * n
    j = 0
    for i in range(0, n, 2):
        res[i] = li[j]
        j += 1
    for i in range(1, n, 2):
        res[i] = li[j]
        j += 1
    print(f'#{T+1}',*res)