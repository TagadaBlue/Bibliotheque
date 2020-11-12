# Generated by Django 2.0.2 on 2019-04-07 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0005_book_book_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_name',
        ),
        migrations.AddField(
            model_name='book',
            name='book_number',
            field=models.IntegerField(default=0, verbose_name='Numéro du tome'),
        ),
    ]
