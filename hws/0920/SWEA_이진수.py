for T in range(int(input())):
    n, li = input().split()
    res = [0] * int(n)
    for i in range(int(n)):
        tmp = bin(int(li[i],16)).lstrip('0b')
        while len(tmp) < 4: tmp = '0' + tmp
        res[i] = tmp
    print(f'#{T+1}', ''.join(res))