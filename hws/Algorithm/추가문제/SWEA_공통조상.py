def dfs(n):
    ret = []
    while n > 0:
        ret.append(n)
        n = P[n]
    return ret

def inorder(v):
    global res
    if v == 0: return
    inorder(L[v])
    res += 1
    inorder(R[v])

for T in range(int(input())):
    v, e, a, b = map(int, input().split())
    tmp = list(map(int, input().split()))
    L, R, P = [0] * (v+1), [0] * (v+1), [0] * (v+1)
    res = 0
    for i in range(0, e * 2, 2):
        p, c = tmp[i], tmp[i+1]
        if L[p] == 0: L[p] = c
        else: R[p] = c
        P[c] = p
    a_li, b_li = dfs(a), dfs(b)
    for i in a_li:
        if i in b_li:
            great_parent = i
            break
    inorder(great_parent)
    print(f'#{T+1}', great_parent, res)