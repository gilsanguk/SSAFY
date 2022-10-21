def solve(lst,square,N,M):
    result=0
    for sqr in square:
        r = sqr[0]
        c = sqr[1]
        length = sqr[2]
        for i in range(r,r+length):
            for j in range(c,c+length):
                try:
                    result += lst[i][j]
                    lst[i][j]=0
                except:
                    pass
 
    return result

for T in range(int(input())):
    N, M = input().split()
    N = int(N)
    M = int(M)
    lst = []
    square = []
    for i in range(N):
        lst.append(list(map(int,input().split())))
    for j in range(M):
        square.append(list(map(int,input().split())))
        
    print(f'#{T+1}', solve(lst,square,N,M))