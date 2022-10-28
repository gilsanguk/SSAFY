def cal(a, b, c):
    if c == '+': return (a + b)
    if c == '-': return (a - b)
    if c == '*': return (a * b)
    return (a / b)

def inorder(k):
    if len(tree[k]) == 1:
        return tree[k][0]
    return cal(inorder(tree[k][1]), inorder(tree[k][2]), tree[k][0])

for T in range(10):
    n = int(input())
    tree = ['0'] * (n+1)
    for i in range(n):
        tmp = list(input().split())
        if not tmp[1].isdecimal(): tree[int(tmp[0])] = (tmp[1], int(tmp[2]), int(tmp[3]))
        else: tree[int(tmp[0])] = (int(tmp[1]),)
    print(f'#{T + 1}', int(inorder(1)))