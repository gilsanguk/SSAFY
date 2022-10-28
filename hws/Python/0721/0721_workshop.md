### 1. 간단한 N의 약수

```python
N = int(input())
for i in range(1,N+1):
    if N%i==0:
        print(i, end=' ')
```

### 2. List의 합 구하기

```python
def list_sum(a):
    return sum(a)
```

### 3. Dictionary로 이루어진 List의 합 구하기

```python
def dict_list_sum(a):
    result = 0
    for i in range(len(a)):
        result += a[i]['age']
    return result
```

### 4. 2차원 List의 전체 합 구하기

```python
def all_list_sum(a):
    result = 0
    for i in range(len(a)):
        for j in range(len(a[i])):
            result += a[i][j]
    return result
```

### 5. 숫자의 의미

```python
def get_secret_word(a):
    result = str()
    for i in range(len(a)):
        result += chr(a[i])
    return result
```

### 6. 내 이름은 몇일까?

```python
def get_secret_number(a):
    result = 0
    for i in range(len(a)):
        result += ord(a[i])
    return result
```

### 7. 강한 이름

```python
def get_strong_word(a,b):
    result_a = 0
    result_b = 0
    for i in range(len(a)):
        result_a += ord(a[i])
    for j in range(len(b)):
        result_b += ord(b[j])
    if result_a>result_b:
        return a
    elif result_a==result_b:
        return a,b
    else:
        return b
```
