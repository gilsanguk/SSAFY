for T in range(int(input())):
    N = int(input())
    lst = list(map(int,input().split()))
    result = 0
    maximum =lst[-1]
    for j in range(N-2,-1,-1):
        if maximum <= lst[j]:
            maximum = lst[j]
        else:
            result+= maximum-lst[j]

    print(f'#{T+1} {result}')