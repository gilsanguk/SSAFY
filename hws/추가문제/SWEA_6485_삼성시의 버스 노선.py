for T in range(int(input())):
    n = int(input())
    li_ab = [0] * n
    for i in range(n):
        a, b = map(int, input().split())
        li_ab[i] = [a,b]
    p = int(input())
    li_c = [0] * p
    li = [0] * p
    for j in range(p):
        li_c[j] = int(input())

    for i in range(n):
        a, b = li_ab[i][0], li_ab[i][1]
        for j in range(p):
            tmp = li_c[j]
            if a <= tmp and tmp <= b:
                li[j] += 1
    result = ' '.join(list(map(str,li)))

    print(f'#{T + 1} {result}')