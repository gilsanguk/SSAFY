for k in range(10):
    T = int(input())
    li = []
    for _ in range(100):
        li.append(list(map(int, input().split())))

    dy = [1, 0, 0]
    dx = [0, 1, -1]
    for i in range(100):
        result = i
        if li[0][i]:
            y = 1
            while y < 100:
                if i != 0:
                    if li[y][i - 1]:
                        i -= 1
                        while (li[y + 1][i]) == 0:
                            i -= 1
                        y += 1
                        continue
                if i != 99:
                    if li[y][i + 1]:
                        i += 1
                        while (li[y + 1][i]) == 0:
                            i += 1
                y += 1
            if li[y-1][i] == 2:
                break

    print(f'#{T} {result}')
