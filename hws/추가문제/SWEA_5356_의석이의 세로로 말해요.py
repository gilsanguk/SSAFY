for T in range(int(input())):
    li = ['']*75
    for i in range(5):
        tmp = list(input())
        for j in range(len(tmp)):
            li[j*5+i] = tmp[j]

    res = ''.join(li)
    print(f'#{T+1} {res}')