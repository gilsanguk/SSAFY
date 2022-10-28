def palindrome(x):
    i = 0
    while x[i] == x[len(x) - i - 1]:
        if i == len(x) // 2:
            return 1
        i += 1
    return 0


def solve(li, n, m):
    for k in range(n):
        for i in range(n - m + 1):
            tmp = ''
            for j in range(i, i + m):
                tmp += li[k][j]
            if palindrome(tmp):
                return tmp
    for k in range(n):
        for i in range(n - m + 1):
            tmp = ''
            for j in range(i, i + m):
                tmp += li[j][k]
            if palindrome(tmp):
                return tmp

            
for T in range(int(input())):
    n, m = map(int, input().split())
    li = list(list(input()) for _ in range(n))
    print(f'#{T + 1} {solve(li, n, m)}')