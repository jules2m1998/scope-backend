# Generated by Django 2.2.13 on 2020-06-22 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20200622_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.EmailField(max_length=50, unique=True),
        ),
    ]
