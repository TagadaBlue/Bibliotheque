# Generated by Django 2.0.2 on 2019-03-22 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manga_name', models.CharField(max_length=200)),
                ('pub_date', models.DateField(verbose_name='Date de sortie')),
            ],
        ),
    ]