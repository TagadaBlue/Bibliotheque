# Generated by Django 2.0.2 on 2019-04-07 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0004_remove_book_book_cover'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_cover',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]