def solve():
    li = list(map(int,input()))
    cnt = 0
    tmp = False
    for i in li:
        if i != int(tmp):
            cnt += 1
            tmp = not tmp
    return cnt


for T in range(int(input())):
    print(f'#{T+1} {solve()}')