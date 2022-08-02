## 01_PJT

### problem_a

#### 학습한 내용

- json의 사용법에 대해서 익힐 수 있었고, open, json.load() 를 이용하여 다른 파일의 값을 불러온다.

- .get()을 통해 dictionary 파일의 value를 가져와서 출력하는 문제이다.

#### 새로 배운 점 및 느낀점

- example을 통해 실습 전에 연습한 내용과 유사하여 쉽게 할 수 있었다.
  

### problem_b

#### 학습한 내용

- .get()으로 불러온 내용을 다른 .json파일에 있는 값에서 찾아서 다른 key에 저장되어있는 value 값으로 바꿔서 출력하는 문제이다.

```python
    genre_names = [] 
    for j in range(len(movie['genre_ids'])):
        for i in genres:
            if i['id'] == movie['genre_ids'][j]:
                genre_names.append(i['name'])
```

- movie.json 파일안 에 있는 딕셔너리 안의 genre_ids 값을 탐색하여  genres.json 안의 id 값과 비교하여 일치하는 값의 장르 'name' 밸류를 할당한다.

#### 어려웠던 부분

- 반복문을 통해 두 파일의 밸류를 비교하는 로직 구현에 시간을 많이 소모했다.

#### 새로 배운 점 및 느낀점

- 구현은 했지만 코드가 정리가 잘 안 되어 있다고 느꼈고, 더 깔끔하게 짤 수 있는 방법이 있을 것 같다.

### problem_c

#### 학습한 내용

- problem_b의 방법을 다중 딕셔너리에 적용하여 여러개의 딕셔너리 자료를 정리하는 문제이다.

```python
    for k in range(len(movies)):
        genre_names = [] 
        for j in range(len(movies[k]['genre_ids'])):
            for i in genres:
                if i['id'] == movies[k]['genre_ids'][j]:
                    genre_names.append(i['name'])
```

- problem_b의 반복문에 반복문 하나를 더 중첩시켜 쉽게 해결하였다.

#### 새로 배운 점 및 느낀점

- 마찬가지로 코드가 난잡하다고 느꼇고 코드를 깔끔하게 정리하는 방법에 대해서도 생각해보아야겠다.

### problem_d

- open 과 .load를 사용하여 새로운 파일을 생성하고, 생성된 파일 안의 딕셔너리 값을 비교하여 정답을 출력하는 문제이다.

```python
        data = open(f'data/movies/{id}.json', encoding='utf-8')
        new_data = json.load(data)
```

- 새로운 

#### 학습한 내용

- 프로그래밍의 가능성은 무한하다는 것을 다시 한 번 느끼게 되었고, 어렵게 느껴지는 만큼 더 학습하고 알고리즘 풀이 등을 통해 실습의 필요성을 느끼게 되었다.
    
- 막힌 부분을 주변의 동기들에게 서로 물어보며 협업의 중요성을 생각해보게 되는 시간이 되었다.

- problem_c를 통해 여러 값을 동시에 불러와 출력하는 방법을 배울 수 있었다.

- problem_d 의 해결과정을 주변 동기들의 풀이법과 비교해보며 max() 함수를 이용하는 법, if문을 이용하는 법, sorted()를 이용하는 법 등 같은 문제를 해결하는 여러가지 방법에 대해서 학습할 수 있었다.

- 전 과정을 학습하며 전 단계에서 작성한 코드를 응용하며 하나의 프로젝트를 완성시켜가는 과정을 알게 되었다.

- open, json.load()를 사용하는 법에 대해서 생각하지 못해 많은 시간을 투자했다.

- 이후에 로직을 짜는 과정에서도 내가 작성해놓은 데이터가 아닌 다른 파일을 불러와서 하다보니 데이터의 컨테이너를 고려한 로직을 짜는데 어려움이 있었다.

- 딕셔너리 안의 리스트, 리스트 안의 딕셔너리 등 중첩된 컨테이너로 되어있는 데이터를 다루는 것이 힘들었다.