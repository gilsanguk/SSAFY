def bin(x,l,r):
    cnt = 1
    while x != (l+r)//2:
        if x < (l+r)//2:
            r = (l+r)//2
            cnt +=1
        else:
            l = (l+r)//2
            cnt +=1
    return cnt

for T in range(int(input())):
    p,a,b = map(int, input().split())
    if bin(a,1,p) < bin(b,1,p):
        print(f'#{T + 1} A')
    elif bin(a,1,p) > bin(b,1,p):
        print(f'#{T + 1} B')
    else:
        print(f'#{T + 1} 0')