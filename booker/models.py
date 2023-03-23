from django.db import models

class Books(models.Model):
    title = models.CharField('제목',max_length=50)
    extent=models.CharField('출판사',max_length=50)
    description=models.TextField('소개',max_length=500)
    charge = models.CharField('가격',max_length=10)
    cover = models.CharField('책표지',max_length=100)
    rights = models.CharField('저자',max_length=50)
    issued_at = models.DateField('출판일자')

    def __str__(self):
        return self.title
