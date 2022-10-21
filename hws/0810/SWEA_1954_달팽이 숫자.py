for T in range(int(input())):
    n = int(input())
    li = [[0 for _ in range(n)] for _ in range(n)]


    def turn(t):
        if t == 3:
            return 0
        return t + 1


    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    cnt = 1

    t, tmp, y, x = 0, 0, 0, 0
    while True:
        if tmp == 2:
            li[y][x] = cnt
            break
        if 0 <= y + dy[t] <= (n - 1) and 0 <= x + dx[t] <= (n - 1) and li[y + dy[t]][x + dx[t]] == 0:
            li[y][x] = cnt
            y, x = y + dy[t], x + dx[t]
            cnt += 1
            tmp = 0
        else:
            t = turn(t)
            tmp += 1

    print(f'#{T + 1}')
    for i in li:
        print(*i)
