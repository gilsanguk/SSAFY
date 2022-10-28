### 1. Type Class

- int, str, list, tuple, dictionary, ...

### 2. Magic Method

- __init__ : 인스턴스 객체가 생성될때 호출되는 메소드
- __str__ : 해당 객체의 출력 형태를 지정
- __del__ : 인스턴스 객체가 소멸되기 직전에 호출되는 메소드
- __repr__ : 어떤 객체의 '출력될 수 있는 표현'을 문자열의 형태로 반환한다.

### 3. Instance Method

- .append() : 리스트의 맨 뒤에 ()안의 요소를 추가시킨다.
- .get() : 딕셔너리의 value 값을 가져온다
- .pop() : 리스트의 맨 마지막 요소를 가져오고 리스트에서 해당 요소를 삭제한다. 

### 4. 오류의 종류

- ZeroDivisionError : 0으로 나눌때 발생
- NameError : 선언되지 않은 변수를 사용할때 발생
- TypeError : 기대하는 자료형이 아니라서 연산을 진행하지 못할 때
- IndexError : 리스트의 범위 밖의 인덱스를 호출할 때
- KeyError : 딕셔너리에 없는 Key를 이용해 호출하려 할때
- ModuleNotFoundError : 설치되어 있지 않은 모듈을 불러오려 할때
- ImportError : 해당 모듈안에 존재하지않는 클래스나 함수를 호출하려 할때