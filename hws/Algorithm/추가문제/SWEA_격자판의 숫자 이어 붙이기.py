dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
def dfs(y, x):
    global res,tmp
    if len(tmp) == 7:
        res.add(tuple(tmp))
        return
    for i in range(4):
        ny, nx = y + dy[i], x + dx[i]
        if 0 <= ny < 4 and 0 <= nx < 4:
            tmp.append(li[ny][nx])
            dfs(ny, nx)
            tmp.pop()

for T in range(int(input())):
    li = [list(map(int,input().split())) for _ in range(4)]
    res = set()
    for y in range(4):
        for x in range(4):
            tmp = [li[y][x]]
            dfs(y, x)
    print(f'#{T+1}', len(res))