for T in range(10):
    n = int(input())
    li = list(map(int, input().split()))
 
    result = 0
    for i in range(2, n - 2):
        if li[i] > li[i - 1] and li[i] > li[i - 2] and li[i] > li[i + 1] and li[i] > li[i + 2]:
            tmp = 255
            for j in range(5):
                if j == 2:
                    continue
                if tmp > (li[i] - li[i - 2 + j]):
                    tmp = (li[i] - li[i - 2 + j])
            result += tmp
 
    print(f'#{T + 1} {result}')