def f(k):
    if k < n:
        f(k*2)
        print(li[k], end='')
        f(k*2+1)

for T in range(int(input())):
    n = int(input()) + 1
    li = [0] * n
    u = [[] for _ in range(n + 1)]
    for i in range(1, n):
        tmp = list(map(str, input().split()))
        li[i] = tmp[1]
    print(f'#{T+1}', end=' ')