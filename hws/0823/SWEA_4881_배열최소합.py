def backtrack(row, tmp, visited):
    global ret
    if tmp > ret:
        return
    if row == n:
        ret = min(ret, tmp)
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            backtrack(row + 1, tmp + li[row][i], visited)
            visited[i] = 0
    return tmp

for T in range(int(input())):
    n = int(input())
    li = [(list(map(int, input().split()))) for _ in range(n)]
    visited = [0]*n
    ret = 2100000000
    backtrack(0, 0, visited)
    print(f'#{T+1} {ret}')