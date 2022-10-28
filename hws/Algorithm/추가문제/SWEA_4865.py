for T in range(int(input())):
    n = str(set(input()))
    m = input()
    dct = {}
    max_v = 0
    for i in n:
        for j in m:
            if i == j:
                if i in dct:
                    dct[i] += 1
                else:
                    dct[i] = 1
    for k,v in dct.items():
        if max_v < v:
            max_v = v

    print(f'#{T+1} {max_v}')