# 1) 부분집합
def syn(a):
    ret = 0
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            ret += li[a[i]][a[j]]+li[a[j]][a[i]]
    return ret
  
def solve(n,li):
    food = []
    minv = 2100000000
    n_set = set(range(n))
    for i in range(1<<(n-1)):
        tmp = []
        for j in range(n):
            if i&(1<<j):
                tmp.append(j)
        if len(tmp) == n//2:
            food.append(tmp)
    for i in range(len(food)):
        res = abs(syn(food[i])-syn(list(n_set-set(food[i]))))
        if minv > res:
            minv = res
    return minv
  
for T in range(int(input())):
    n = int(input())
    li = []
    for _ in range(n):
        li.append(list(map(int, input().split())))
  
    print(f'#{T+1} {solve(n,li)}')

###########################################################################
# 2) 백트래킹 (조합)
def backtrack(depth, idx):
    global res
    if depth == (n >> 1):
        A, B = 0, 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:
                    A += food[i][j]
                elif not visited[i] and not visited[j]:
                    B += food[i][j]
        res = min(res, abs(A-B))
        return
 
    for k in range(idx, n):
        visited[k] = True
        backtrack(depth+1, k+1)
        visited[k] = False
 
for T in range(int(input())):
    n = int(input())
    food = [list(map(int,input().split())) for _ in range(n)]
    visited = [False] * n
    res = 7654321
    backtrack(0, 0)
    print(f'#{T + 1}', res)