dct = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
       '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

for T in range(int(input())):
    n, m = map(int, input().split())
    password, res, i, j = 0, [0] * 9, m - 1, 8
    for _ in range(n):
        tmp = input()
        if int(tmp): password = tmp
    while i:
        if int(password[i]):
            res[j] = dct[password[i - 6:i + 1]]
            i, j = i - 6, j - 1
        else: i -= 1
    tmp = 0
    for i in range(1, 9):
        tmp += res[i] + res[i] * (i & 1) * 2
    if tmp%10: print(f'#{T + 1}', 0)
    else: print(f'#{T + 1}', sum(res))