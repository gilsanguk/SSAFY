def even(i, j):
    tmp = 0
    k = 1
    while li[i][j - k] == li[i][j + k - 1]:
        tmp += 2
        k += 1
        if j - k < 0 or j + k - 1 > 99:
            return tmp
    return tmp


def odd(i, j):
    tmp = 1
    k = 1
    while li[i][j - k] == li[i][j + k]:
        tmp += 2
        k += 1
        if j - k < 0 or j + k > 99:
            return tmp
    return tmp

def c_even(i, j):
    tmp = 0
    k = 1
    while li[i-k][j] == li[i+k-1][j]:
        tmp += 2
        k += 1
        if i - k < 0 or i + k - 1 > 99:
            return tmp
    return tmp


def c_odd(i, j):
    tmp = 1
    k = 1
    while li[i-k][j] == li[i+k][j]:
        tmp += 2
        k += 1
        if i - k < 0 or i + k > 99:
            return tmp
    return tmp



for _ in range(10):
    T = int(input())
    li = []
    for _ in range(100):
        li.append(list(input()))
    cnt = 0
    for i in range(100):
        for j in range(1, 99):
            if cnt < even(i, j):
                cnt = even(i, j)
            if cnt < odd(i, j):
                cnt = odd(i, j)

    for j in range(100):
        for i in range(1, 99):
            if cnt < c_even(i, j):
                cnt = c_even(i, j)
            if cnt < c_odd(i, j):
                cnt = c_odd(i, j)

    print(f'#{T} {cnt}')
