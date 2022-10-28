def dfs(n):
    global visited
    visited.add(n)
    if n not in dct:
        return
    for i in dct[n]:
        if i not in visited:
            dfs(i)

for T in range(int(input())):
    e, n = map(int,input().split())
    tmp = list(map(int,input().split()))
    dct, visited = {}, set()
    for i in range(0, e*2, 2):
        if tmp[i] in dct: dct[tmp[i]].append(tmp[i+1])
        else: dct[tmp[i]] = [tmp[i+1]]
    dfs(n)
    print(f'#{T+1}', len(visited))