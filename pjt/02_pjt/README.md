## 02_PJT

### problem_a

#### 학습한 내용

- api key를 통해서 웹사이트의 api를 requests.get(url) 을 이용하여 데이터를 가져온다.

- 가져온 데이터를 .json()을 통해 파이썬에서 쓸수 있는 데이터(딕셔너리)로 가공시킨다.

#### 어려웠던 부분

- api를 통해 받는 것이 익숙치 않아 내용 이해가 오래걸렸다.

### problem_b

#### 학습한 내용

- requests.get()으로 불러온 내용을 가공하여 생성한 딕셔너리에서 필요한 데이터 만을 가져온다.

```python
 return [eight for eight in response['results'] if eight['vote_average'] >= 8.0]
```

#### 새로 배운 점 및 느낀점

- .json()에 대해서 어렵게 생각하지 않고, 가상의 딕셔너리가 있다는 것을 머리속으로 생각하고 하니 수월하게 된 것 같다.

### problem_c

#### 학습한 내용

- problem_b에 이어 데이터를 정리하는 과정의 심화이다.

```python
return sorted([(movie ['title'], movie ['vote_average']) for movie in response['results']], key=lambda x:x[1], reverse=True)[:6]
```

- problem_b처럼 list comprehension을 통해 자료를 받은뒤 sorted함수를 이용하여 딕셔너리의 value순으로 정렬하고(lambda 사용) 원하는 만큼 반환하였다.

### problem_d

- requests.get()을 이용하여 가져온 데이터를 이용하여 한번더 requests.get()으로 api를 호출해 다시 한 번 데이터를 가져온다.

```python
        response = requests.get(URL,params=params).json()
        movie_id = response['results'][0]['id']

        URL_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/recommendations'
        response_2 = requests.get(URL_2,params=params).json()
```

- 가져온 데이터의 일부분을 가공하여 필요한 데이터만 변수에 할당하고, 변수를 이용하여 다시한번 api를 호출하는 방법으로 해결할 수 있다.

- list comprehension을 이용해 정리하여 반환한다. 

```python
        return [movie['title'] for movie in response_2['results']]
```

#### 새로 배운 점 및 느낀점

- 한번 더 url을 호출하는 과정에서 params을 다시 한번 할당해주면 된다는 것을 알았다.

- 가져온 데이터를 가공하여 다시 api호출이 가능하다는 것을 배웠다.

### problem_e

- 마찬가지로 가져온 데이터를 이용하여 한번더 api를 호출해 다시 한 번 데이터를 가져온다.

```python
        response = requests.get(URL,params=params).json()
        movie_id = response['results'][0]['id']

        URL_2 = f'https://api.themoviedb.org/3/movie/{movie_id}/credits'
        response_2 = requests.get(URL_2,params=params).json()
```

- list comprehension을 이용해 정리하여 반환한다. 문제에서 요구하는 형식에 맞춰 딕셔너리 안에 두 개의 리스트를 생성하여 반환한다.

```python
        return {'cast':[person['name'] for person in response_2['cast'] if person['cast_id']<10], 'directing':[person['name'] for person in response_2['crew'] if person['department']=='Directing']}
```

#### 새로 배운 점 및 느낀점

- 지난주의 json() 실습으로 많이 익숙해져서 어렵지 않게 해결했던 것 같다.