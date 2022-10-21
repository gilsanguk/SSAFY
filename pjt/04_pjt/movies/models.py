from django.db import models

# Create your models here.
class Movie(models.Model):    #테이블 이름은 appname_classname
    #primary key ==> id라는 필드가 자동으로 생성 / unique 값
    #필드 정의 ==> 이름 = 필드타입()
    title = models.CharField(max_length=20)
    audience = models.IntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()

    def __str__(self):
        return f'{self.id}번 영화 - {self.title} / {self.audience}'