def init():
    for i in range(1, n + 1):
        tree[i] = tmp[i - 1]
        while i > 1:
            if tree[i] < tree[i >> 1]:
                tree[i], tree[i >> 1] = tree[i >> 1], tree[i]
            i >>= 1

def getsum(k):
    ret = 0
    while k > 1:
        k >>= 1
        ret += tree[k]
    return ret

for T in range(int(input())):
    n = int(input())
    tree = [0] * (n + 1)
    tmp = list(map(int, input().split()))
    init()
    print(f'#{T+1}', getsum(n))