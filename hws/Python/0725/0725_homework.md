### 1. 모음은 몇 개나 있을까?

```python
def count_vowels(str):
    cnt = 0
    for vowel in ['a','e','i','o','u']:
        cnt+=str.count(vowel)
    return cnt
```

### 2. 문자열 조작

- (4) : 특정 문자를 지정하지 않으면 공백을 제거한다.

### 3. 정사각형만 만들기

```python
def only_square_area(hight,width):
    area = []
    for h in hight:
        for w in width:
            if h == w:
                area.append(h*w)
    return area

print(only_square_area([32,55,63],[13,32,40,55]))
```

