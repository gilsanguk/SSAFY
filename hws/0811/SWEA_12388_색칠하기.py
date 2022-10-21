for T in range(int(input())):
    n = int(input())
    li = [(list(map(int, input().split()))) for _ in range(n)]
    lst = [[0] * 10 for _ in range(10)]
    for i in li:
        for j in range(i[1], i[3] + 1):
            for k in range(i[0], i[2] + 1):
                lst[j][k] += i[4]
    cnt = 0
    for i in lst:
        for j in i:
            if j == 3:
                cnt += 1
    print(f'#{T + 1} {cnt}')
