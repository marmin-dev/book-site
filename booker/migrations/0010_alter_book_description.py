# Generated by Django 4.1.7 on 2023-03-27 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0009_alter_comment_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='description',
            field=models.TextField(max_length=500, verbose_name='소개'),
        ),
    ]
