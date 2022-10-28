def divide(s, e, d):
    if s == e: return 1
    mid = (s+e) >> 1
    if A[mid] < num:
        if d == -1: return 0
        return divide(mid + 1, e, -1)
    if A[mid] > num:
        if d == 1: return 0
        return divide(s, mid - 1, 1)
    else: return 1

for T in range(int(input())):
    n, m = map(int,input().split())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    A.sort()
    B = list(set(A)&set(B))
    res = 0
    for num in B:
        res += divide(0, len(A) - 1, 0)
    print(f'#{T+1}', res)