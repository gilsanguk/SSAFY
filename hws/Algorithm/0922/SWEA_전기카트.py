def solve(k, now, tmp):
    global res
    if k == n:
        res = min(res, tmp + li[now][0])
        return
    if tmp > res: return
    for i in range(1, n):
        if i == now: continue
        if not visited[i]:
            visited[i] = True
            solve(k+1, i, tmp + li[now][i])
            visited[i] = False

for T in range(int(input())):
    n = int(input())
    li = [list(map(int,input().split())) for _ in range(n)]
    visited = [False] * (n)
    res = 987654321
    solve(1, 0, 0)
    print(f'#{T+1}', res)