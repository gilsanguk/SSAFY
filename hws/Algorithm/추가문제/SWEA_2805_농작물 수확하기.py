def solve():
    mid = n//2+1
    ret =0
    for y in range(n):
        l, r = abs(mid-(y+1)), n-abs((mid-(y+1)))
        for x in range(l,r):
            ret += li[y][x]
    return ret

for T in range(int(input())):
    n = int(input())
    li = [list(map(int,input())) for _ in range(n)]
    print(f'#{T+1} {solve()}')