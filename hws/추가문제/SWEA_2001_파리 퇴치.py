def flyhit(lst,r,c,m):
    result = 0
    for i in range(r,r+m):
        for j in range(c,c+m):
            result += lst[i][j]
    return result


for T in range(int(input())):
    n, m = map(int,input().split())
    li = [(list(map(int, input().split()))) for _ in range(n)]
    result = 0
    for r in range(n-m+1):
        for c in range(n-m+1):
            tmp = flyhit(li, r, c, m)
            if result < tmp:
                result = tmp

    print(f'#{T + 1} {result}')