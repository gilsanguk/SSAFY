for T in range(int(input())):
    n, q = map(int,input().split())
    li = [0] * n
    for i in range(q):
        a, b = map(int, input().split())
        for j in range(a-1,b):
            li[j]= i+1

    result = ' '.join(list(map(str,li)))

    print(f'#{T + 1} {result}')