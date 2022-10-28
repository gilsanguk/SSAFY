def rsp(a,b):
    if li[a] == li[b]:
        return a
    if li[a] < li[b]:
        a, b = b, a
    if li[a] == 3 and li[b] == 1:
        return b
    return a

def backtrack(s, e):
    if s+1 == e:
        return rsp(s, e)
    if s == e:
        return s
    mid = (s + e) // 2
    return rsp(backtrack(s, mid), backtrack(mid+1, e))

for T in range(int(input())):
    n = int(input())
    li = list(map(int, input().split()))
    res = backtrack(0, n - 1) + 1
    print(f'#{T+1} {res}')