dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
def othello(y, x, c):
    board[y][x] = c
    res = set()
    for i in range(8):
        ny, nx = y + dy[i], x + dx[i]
        tmp = set()
        while 0 <= ny < n and 0 <= nx < n and board[ny][nx]:
            if board[ny][nx] == c: 
                res |= tmp
                break
            else: 
                tmp.add((ny,nx))
            ny, nx = ny + dy[i], nx + dx[i]
    for y, x in res: board[y][x] = c


for T in range(int(input())):
    n, m = map(int, input().split())
    board = [[0] * n for _ in range(n)]
    board[(n >> 1) - 1][(n >> 1) - 1] = board[n >> 1][n >> 1] = 2
    board[n >> 1][(n >> 1) - 1] = board[(n >> 1) - 1][n >> 1] = 1
    for _ in range(m):
        x, y, c = map(int, input().split())
        othello(y - 1, x - 1, c)
    a, b = 0, 0
    for row in board:
        a, b = a + row.count(1), b + row.count(2)
    print(f'#{T + 1}', a, b)