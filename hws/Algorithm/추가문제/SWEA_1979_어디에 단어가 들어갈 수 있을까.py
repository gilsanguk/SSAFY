for T in range(int(input())):
    n, m = map(int, input().split())
    li = [(list(map(int, input().split()))) for _ in range(n)]
    result = []
    cnt = 0
    for i in range(n):
        j = 0
        tmp = 0
        while j < n:
            if li[j][i]:
                while j < n and li[j][i]:
                    tmp+=1
                    j+=1
                result.append(tmp)
                tmp = 0
            j+=1
    for j in range(n):
        i = 0
        tmp = 0
        while i < n:
            if li[j][i]:
                while i < n and li[j][i]:
                    tmp += 1
                    i += 1
                result.append(tmp)
                tmp = 0
            i += 1
    for i in result:
        if i == m:
            cnt+=1

    print(f'#{T + 1} {cnt}')