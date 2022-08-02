### 1. Buit-in 함수와 메서드
- .sort() # 리스트 a의 원본값이 [1,2,3]로 정렬
- sorted() # 원본값은 바뀌지않음
```python
a=[1,3,2]
a.sort() # print(a) = [1,2,3]
sorted(a) # print (a) = [1,3,2]
```

### 2. .extend()와 .append()
- .append() # iterable 그 자체를 원소로 추가함
- .extend() # iterable 안의 원소들을 추가함.
```python
a = [1,2,3]
b = 'hello'
a.append(b) # [1,2,3,'hello']
a.extend(b) # [1,2,3,'h','e','l','l','o']
```

### 3. 복사가 잘 된건가?
- a와 b에 담긴 list의 요소는 같다.
- b=a를 실행할 때 b가 a의 주소를 복사해 가져오기 때문에 b와 a는 같은 list 값을 가리키게 된다.
- 따라서 a나 b 어떤것의 요소값을 변경하면 다른 한쪽도 변경된다.