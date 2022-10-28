### 1. pip

(1) 파이썬의 Faker라는 라이브러리를 설치하기 위한 코드

(2) 터미널에서 실행해야 한다.

### 2. Basic Usages

```python
from faker import Faker # 1 faker 모듈에서 Faker 클래스를 가져오기 위한 코드
fake = Faker() # 2 Faker는 클래스, fake는 인스턴스변수이다.
fake.name() # 3 name()은 fake의 메서드이다.
```

### 3. Localization

```python
class Faker():
  
  def __init__(self,locale='en_US'):
    pass
```

### 4. Seeding the Genenrator

```python
fake1 = Faker('ko_KR')
Faker.seed(87654321)

print(fake1.name())      # 1 이진호

fake2 = Faker('ko_KR')
print(fake2.name())      # 2 강은주
```

- seed() : 클래스 메서드

```python
fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)

print(fake1.name())      # 1 이진호

fake2 = Faker('ko_KR')
print(fake2.name())      # 2 랜덤 난수
```

- seed_instance() : 인스턴스 메서드