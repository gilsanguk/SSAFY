for T in range(int(input())):
    n = int(input())
    li = [(list(map(int,input().split()))) for _ in range(n)]
    li.sort(key=lambda x: (x[1],x[0]))
    res = [li[0]]
    for i in li:
        if res[-1][1] <= i[0]: res.append(i)
    print(f'#{T+1}', len(res))