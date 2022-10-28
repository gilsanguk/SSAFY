dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
def bfs():
    for _ in range(m):
        dct = {}
        for i in range(len(q)):
            y, x, num, d = q[i]
            if num == 0: continue
            ny, nx = y + dy[d], x + dx[d]
            if ny == 0 or ny == n - 1 or nx == 0 or nx == n - 1:
                num >>= 1
                d = (d + 2) % 4
            q[i] = [ny, nx, num, d]
 
            if (ny, nx) not in dct:
                dct[(ny, nx)] = (i, num, d)
            else:
                past_i, past_num, past_d = dct[(ny, nx)]
                if past_num < num:
                    q[i][2] += q[past_i][2]
                    q[past_i] = (0, 0, 0, 0)
                    dct[(ny, nx)] = (i, num, d)
                else:
                    q[past_i][2] += q[i][2]
                    q[i] = (0, 0, 0, 0)
                    dct[(ny, nx)] = (past_i, past_num, past_d)
 
for T in range(int(input())):
    n, m, k = map(int, input().split())
    res, q = 0, []
    for i in range(k):
        y, x, num, d = map(int, input().split())
        if d == 2 : d = 3
        elif d == 3: d = 2
        q.append([y, x, num, d - 1])
    bfs()
    for i in range(len(q)): res += q[i][2]
    print(f'#{T + 1}', res)