# Generated by Django 2.2.13 on 2020-06-21 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='person',
            name='number',
            field=models.IntegerField(blank=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='sex',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
