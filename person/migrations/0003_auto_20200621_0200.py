# Generated by Django 2.2.13 on 2020-06-21 02:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_auto_20200621_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birth_day',
            field=models.DateField(blank=True),
        ),
    ]
