# Generated by Django 3.1.3 on 2020-11-09 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mangas', '0016_auto_20200521_2141'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ('book_number',)},
        ),
        migrations.AlterModelOptions(
            name='manga',
            options={'ordering': ('manga_name',)},
        ),
        migrations.AlterField(
            model_name='book',
            name='book_name',
            field=models.CharField(blank=True, default=' ', max_length=200, verbose_name='Nom du tome'),
        ),
        migrations.AlterField(
            model_name='manga',
            name='manga_cover',
            field=models.FileField(blank=True, null=True, upload_to='mangas/images'),
        ),
    ]
