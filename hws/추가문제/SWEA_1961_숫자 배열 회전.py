import sys;sys.stdin = open('input.txt')

def nin(li):
    res = []
    for i in range(n):
        tmp = ''
        for j in range(n-1,-1,-1):
            tmp += str(li[i][j])
        res.append(tmp)
    return res

def hun(li):
    res = []
    for i in range(n-1,-1,-1):
        tmp = ''
        for j in range(n-1,-1,-1):
            tmp += str(li[i][j])
        res.append(tmp)
    return res
def twh(li):
    res = []
    for i in range(n-1,-1,-1):
        tmp = ''
        for j in range(n):
            tmp += str(li[i][j])
        res.append(tmp)
    return res

for T in range(int(input())):
    n = int(input())
    li = [(list(map(int, input().split()))) for _ in range(n)]
    zip_li = list(zip(*li))
    a,b,c = nin(zip_li), hun(li), twh(zip_li)
    print(f'#{T+1}')
    for i in range(n):
        print(f'{a[i]} {b[i]} {c[i]}')