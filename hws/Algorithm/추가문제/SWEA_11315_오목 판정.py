def row(r, c):
    if c > n-5:
        return 0
    for i in range(1, 5):
        if li[r][c + i] != li[r][c]:
            return 0
    return 1

def col(r, c):
    if r > n-5:
        return 0
    for i in range(1, 5):
        if li[r + i][c] != li[r][c]:
            return 0
    return 1


def l_dia(r, c):
    if r > n-5 or c > n-5:
        return 0
    for i in range(1, 5):
        if li[r + i][c + i] != li[r][c]:
            return 0
    return 1


def u_dia(r, c):
    if r < 4 or c > n-5:
        return 0
    for i in range(1, 5):
        if li[r - i][c + i] != li[r][c]:
            return 0
    return 1


def solve():
    for r in range(n):
        for c in range(n):
            if li[r][c] == 'o':
                if row(r, c) or col(r, c) or l_dia(r, c) or u_dia(r, c):
                    return 'YES'
    return 'NO'



for T in range(int(input())):
    n = int(input())
    li = [list(input()) for _ in range(n)]
    print(f'#{T+1} {solve()}')