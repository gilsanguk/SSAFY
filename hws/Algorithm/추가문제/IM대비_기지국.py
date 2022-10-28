dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def f(y, x, k):
    for j in range(1, k + 1):
        for i in range(4):
            ny, nx = y + j * dy[i], x + j * dx[i]
            if 0 <= ny < n and 0 <= nx < n and li[ny][nx] == 'H':
                li[ny][nx] = 'X'


def solve():
    cnt = 0
    for y in range(n):
        for x in range(n):
            if li[y][x] != 'X' and li[y][x] != 'H':
                tmp = ord(li[y][x]) - ord('A') + 1
                f(y, x, tmp)

    for y in range(n):
        for x in range(n):
            if li[y][x] == 'H':
                cnt += 1
    return cnt


for T in range(3):
    n = int(input())
    li = [list(input()) for _ in range(n)]
    print(f'#{T + 1} {solve()}')