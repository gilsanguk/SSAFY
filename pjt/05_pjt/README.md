# 길상욱

## 04_PJT

### Model, URL, View, Admin

#### 학습한 내용

- models.py 에 Movie 모델 클래스를 정의하여 title, audience 등의 필드를 만든다.

- 프로젝트 폴더의 urls.py에 include를 하고, 앱 내에 urls.py 를 만들어 index, new, create 등의 url 요청에 맞는 path를 생성한다.

- views.py에 각각의 함수를 정의하고 url 요청에 따른 역할을 구현한다.

- views.py에 데코레이터를 이용하여 허용 http method를 지정해준다.

#### 새로 배운 점 및 느낀점

- 저번 관통과 비슷한 내용이었다.

- 많이 어려웠던 저번과 달리 반복때문인지 훨씬 수월했던 것 같다.

### Admin, Form

- admin.site.register()를 이용하여 모델을 어드민 사이트에 등록한다.

- forms.py에 모델폼을 생성한다. models.py에 있는 모델을 이용하여 필드를 처리한다.

### Template

#### 학습한 내용

- base.html, index.html, detail.html, new.html, edit.html 을 각각 생성한다.

### A. base.html

#### 학습한 내용

- 공통 부모 템플릿으로 기본 html 스켈레톤 코드에 부트스트랩 CDN만 추가하여 만들었다.

### B. index.html

#### 학습한 내용

- 데이터베이스 테이블에 존재하는 영화의 목록을 표시한다.

- 각각의 영화 제목을 통해 상세 정보 (detail.html)로 이동하고, create 버튼을 통해 새로운 영화의 정보를 등록할 수 있다.
```html
<div class="d-flex justify-content-center">
  <div class="col-10">
      <h1>INDEX</h1>
      <a href="{% url 'movies:create' %}">Create</a>
      <hr>
      {% for movie in movies %}
      <a href="{% url 'movies:detail' movie.pk %}">{{ movie.title }}</a>
      <p>{{ movie.score }}</p>
      <hr>
      {% endfor %}
  </div>
</div>
```

- 기본 페이지로 크게 어려운 부분은 없었다.

- 부트스트랩 클래스를 이용하여 css를 넣었다.

### C. detail.html

#### 학습한 내용

- index.html 에서 영화의 제목에 걸려있는 링크를 눌러 들어오면 상세정보를 표시해준다.

- bootstrap card 컴포넌트를 이용하여 영화의 상세 정보를 표시한다.

- 수정 및 삭제를 할 수 있는 버튼을 표시해준다.

- index페이지로 이동하는 버튼을 표시한다.
```html
<div class="container mb-5">
  <div class="row">
    <h1 class = "d-flex justify-content-center">DETAIL</h1>
    <hr> 
  </div>
  <div class= "d-flex justify-content-center">
    <div class="card" style="width: 25rem;">
      <img src="{{ movie.poster_url }}" class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">{{ movie.title }}</h5>
        <p class="card-text">Audience : {{ movie.audience }}</p>
        <p class="card-text">Release Dates : {{ movie.release_date|date:"M, d, Y" }}</p>
        <p class="card-text">Genre : {{ movie.genre }}</p>
        <p class="card-text">Score : {{ movie.score }}</p>
        <p class="card-text">{{ movie.description }}</p>
        <a href="{% url 'movies:update' movie.pk %}" class="btn btn-info">UPDATE</a>
        <form action="{% url 'movies:delete' movie.pk %}" method="POST" class="d-inline">
          {% csrf_token %}
          <button class="btn btn-danger">DELETE</button>
        </form>
      </div>
    </div>
  </div>
  <a href="{% url 'movies:index' %}" class="btn btn-warning">BACK</a>
</div>
```

#### 어려웠던 점

- 어려움은 크지 않았고, 부트스트랩 사용법이 잘 기억나지 않아 오래걸렸다.

### D. Create.html

#### 학습한 내용

- forms.py에 만들어뒀던 form 요소를 통해 특정 영화를 생성할 수 있다.

- label, input, select 등을 이용하여 구현한다.

- 하단에는 submit 버튼을 통해 db table에 저장하여 index.html에 출력할 수 있게 한다.
```html
<div class="d-flex justify-content-center mb-3">
  <div class="col-10">
    <h1>CREATE</h1>
    <hr>
    <form action="{% url 'movies:create' %}" method="POST">
      {% csrf_token %}
      {{form.as_p}}
      <button class="btn btn-primary" type="submit">Submit</button>
    </form>
    <hr>
    <a href="{% url 'movies:index' %}" class="btn btn-info">BACK</a>
  </div>
</div>
```

#### 어려웠던 점

- forms.py에 클래스나 widget 속성등을 넘기는 것이 직관적으로 잘 이해되지 않아 어려움을 겪었다.

- 마찬가지로 css 적용이 오래걸렸다.

### E. update.html

#### 학습한 내용

- create.html과 동일하게 구성하지만, reset버튼과 현재 db table 에 저장된 값을 디폴트로 띄워야 한다.

-----
# 김원웅

1. 모델 폼 활용법을 배울 수 있었다.
2. 부트스트랩을 통해 사용자 화면의 가독성을 높일 수 있었다.
3. 겟과 포스트의 차이를 확실히 학습하였다.