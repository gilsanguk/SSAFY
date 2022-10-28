for T in range(int(input())):
    p = input()
    t = input()
    res = 0
    for i in range(len(p)):
        tmp = 0
        for j in range(len(t)):
            if p[i] == t[j]:
                tmp += 1
        if res < tmp:
            res = tmp
    print(f'#{T+1} {res}')