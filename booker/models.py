from django.db import models
from django.contrib.auth.models import User

class Book(models.Model):
    title = models.CharField('제목',max_length=50,unique=True,null=False)
    extent=models.CharField('출판사',max_length=50)
    description=models.TextField('소개',max_length=500)
    charge = models.CharField('가격',max_length=10)
    cover = models.CharField('책표지',max_length=100)
    rights = models.CharField('저자',max_length=50)
    issued_at = models.CharField('출판일자',max_length=20)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField('내용',max_length=255)
    post = models.ForeignKey(Book,on_delete=models.CASCADE)
    create_at = models.DateTimeField()
    def __str__(self):
        return self.content
