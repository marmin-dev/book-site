# Generated by Django 4.1.7 on 2023-03-26 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('booker', '0008_alter_book_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-create_at']},
        ),
    ]
