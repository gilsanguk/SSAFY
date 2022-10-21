for T in range(int(input())):
    n = int(input())
    li = [2, 3, 5, 7, 11]
    result = [0, 0, 0, 0, 0]
    for i in range(5):
        while (n % li[i]) == 0:
            n = n // li[i]
            result[i] += 1

    sol = ' '.join(list(map(str,result)))

    print(f'#{T + 1} {sol}')