# 길상욱

## 04_PJT

### Model, URL, View, Admin

#### 학습한 내용

- models.py 에 Movie 모델 클래스를 정의하여 title, audience 등의 필드를 만든다.

- 프로젝트 폴더의 urls.py에 inclue=de를 하고, 앱 내에 urls.py 를 만들어 index, new, create 등의 url 요청에 맞는 path를 생성한다.

- views.py에 각각의 함수를 정의하고 url 요청에 따른 역할을 구현한다.

#### 새로 배운 점 및 느낀점

- 어제 배웠던 내용으로 다시 한 번 복습하는 마음으로 구현하였다.

### Template

#### 학습한 내용

- base.html, index.html, detail.html, new.html, edit.html 을 각각 생성한다.

### A. base.html

#### 학습한 내용

- 공통 부모 템플릿으로 기본 html 스켈레톤 코드에 부트스트랩 CDN만 추가하여 만들었다.

### B. index.html

#### 학습한 내용

- 데이터베이스 테이블에 존재하는 영화의 목록을 표시한다.

- 각각의 영화 제목을 통해 상세 정보 (detail.html)로 이동하고, new 버튼을 통해 새로운 영화의 정보를 등록할 수 있다.
```django
<h1>Index</h1>
<a href="{% url 'movies:new' %}">[New]</a>
<hr>
{% for movie in movies %}
<div>
  <p><a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a></p>
  <p>{{ movie.score }}</p>
</div>
  <hr>
{% endfor %}
```

- 기본 페이지로 크게 어려운 부분은 없었다.

### C. detail.html

#### 학습한 내용

- index.html 에서 영화의 제목에 걸려있는 링크를 눌러 들어오면 상세정보를 표시해준다.

- html form 요소를 이용하여 영화의 이미지, 타이틀 등 정보를 표시한다.

- 하단에는 edit.html 로 이동하는 링크, 영화의 데이터를 삭제하는 버튼, index.html로 돌아가는 링크로 이루어져 있다.

#### 어려웠던 점

- edit, delete등을 구현하는 부분에 기억이 잘 안나서 조금 오래걸렸다.

### D. new.html

#### 학습한 내용

- form 요소를 통해 특정 영화를 생성할 수 있다.

- label, input, select 등을 이용하여 구현한다.

- 하단에는 submit 버튼튼을 통해 db table에 저장하여 index.html에 출력할 수 있게 한다.

#### 어려웠던 점

- select, input 등의 밸류나 타입 등을 조정하여 구현해야 했는데, html을 배웠던 것이 잘 기억나지 않아서 구글링 등을 통해 구현하였다.

#### 새로 배운 점 및 느낀점

- html에서 배울 때는 정적이라고 느껴졌는데 데이터를 요청,출력하는 과정을 더하니 동적인 느낌이 났다.

### E. new.html

#### 학습한 내용

- edit.html과 동일하게 구성하지만, reset버튼과 현재 db table 에 저장된 값을 디폴트로 띄워야 한다.
```django
    <label for="release_date">RELEASE_DATE</label>
    <input type="date" name="release_date" id="release_date" value = {{movie.release_date|date:"o-m-d"}}>

    <label for="genre">GENRE</label>
    <select name="genre" id="genre">
      {% for genre in genres %}
      {% if genre == movie.genre %}
      <option value={{genre}} selected>{{genre}}</option>
      {% else %}
      <option value={{genre}}>{{genre}}</option>
      {% endif %}
      {% endfor %}
    </select>
```

#### 어려웠던 점

- value를 이용하여 구현하는 것이 날짜에서도 달랐고, select를 이용한 부분은 for 문과 if 문으로 구현하여야 했어서 처음에 감이 잘 오지 않았다.

-----
# 김원웅

1.첫 페어코딩이라 신선하고 재밌었다
2.내가 미처 생각못한 부분을 페어가 채워주었다
3.날짜 값을 표시하는데에 어려움을 겪었다
