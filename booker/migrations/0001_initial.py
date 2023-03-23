# Generated by Django 4.1.7 on 2023-03-23 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='제목')),
                ('extent', models.CharField(max_length=50, verbose_name='출판사')),
                ('description', models.TextField(max_length=500, verbose_name='소개')),
                ('charge', models.CharField(max_length=10, verbose_name='가격')),
                ('cover', models.CharField(max_length=100, verbose_name='책표지')),
                ('rights', models.CharField(max_length=50, verbose_name='저자')),
                ('issued_at', models.CharField(max_length=20, verbose_name='출판일자')),
            ],
        ),
    ]
