### 1. 무엇이 중복일까
```python
def duplicated_letters(string):
    lst = set()
    for i in string:
        if string.count(i) > 1:
            lst.add(i)
    return list(lst)

print(duplicated_letters('apple'))
print(duplicated_letters('banana'))
```

### 2. 소대소대
```python
def low_and_up(string):
    lst = []
    for i in range(len(string)):
        if i%2:
            lst.append(string[i].upper())
        else:
            lst.append(string[i].lower())
    return ''.join(lst)

print(low_and_up('apple'))
print(low_and_up('banana'))
```

### 3. 솔로 천국 만들기
```python
def lonely(lst):
    result=[]
    for i in range(len(lst)-1):
        if lst[i] != lst[i+1]:
            result.append(lst[i])
    result.append(lst[-1])

    return result

print(lonely([1,1,3,3,0,1,1]))
print(lonely([4,4,4,3,3]))
```